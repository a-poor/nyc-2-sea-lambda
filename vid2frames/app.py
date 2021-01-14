
import io
import re
from pathlib import Path
from os.path import splitext

import cv2
import boto3

def lambda_handler(event,context):
    S3 = boto3.client("s3")
    BUCKET_IN = "nyc2sea-rawvideo"
    BUCKET_OUT = "nyc2sea-rawimages"
    TMP_DIR = Path("/tmp")
    p_vid = TMP_DIR / "video.mp4"
    
    # Get new objects' keys
    obj_keys = get_video_keys(event)
    
    # For each object
    for k in obj_keys:
        # Download the video
        download_video(S3,BUCKET_IN,k,p_vid)
        save_frames(S3,BUCKET_OUT,k,p_vid)

def get_video_keys(event):
    return [r["s3"]["object"]["key"] for r in event["Records"]]

def download_video(s3,bucket,key,fn):
    s3.download_file(str(bucket),str(key),str(fn))

def get_vid_frames(path):
    vid = cv2.VideoCapture(str(path))
    while True:
        success, image = vid.read()
        if not success: break
        yield image

def img_to_buff(img,ext=".jpg"):
    success, buff = cv2.imencode(ext,img)
    return io.BytesIO(buff)

def upload_fo(s3,bucket,key,fo):
    s3.upload_fileobj(fo,bucket,key)

def save_frames(s3,bucket,vid_key,vid_path):
    newkey = re.sub(r" ","",vid_key.upper())
    base = splitext(newkey)[0]
    fn = lambda i: f"{base}-{i:05d}.JPG"
    for i, img in enumerate(get_vid_frames(vid_path)):
        fo = img_to_buff(img)
        upload_fo(s3,bucket,fn(i),fo)

