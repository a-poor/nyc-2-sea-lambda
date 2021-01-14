
import os
import io
import json
import hashlib
from pathlib import Path

import boto3
from process_image import process_image

"""
process_image(path,crop=(195,1020,1500,1080),cuttoff=200)
"""


def lambda_handler(event,context):
    S3 = boto3.client("s3")
    BUCKET_IN = "nyc2sea-rawimages"
    BUCKET_OUT = os.environ.get("BUCKET_OUT","nyc2sea-ocrdata")
    
    CROP = (195,1020,1500,1080) # Set with ENV?
    CUTTOFF = 200               # Set with ENV?
    
    print("Starting...")

    img_path = Path("/tmp/img.jpg")    

    results = []
    for k in get_image_keys(event):
        download_image(S3,BUCKET_IN,k,img_path)
        txt = process_image(img_path,CROP,CUTTOFF)
        data = {"bucket":BUCKET_IN,"key":k,"ocr-data":txt}
        sdata = json.dumps(data)
        fn = get_key(sdata)
        fo = io.BytesIO(sdata.encode())
        S3.upload_fileobj(fo,BUCKET_OUT,fn)
        print(f"Uploaded: s3://{BUCKET_OUT}/{fn}")
    print("Done.")

def get_image_keys(event):
    return [r["s3"]["object"]["key"] for r in event["Records"]]

def download_image(s3,bucket,key,fn):
    s3.download_file(bucket,key,str(fn))

def get_hash(s: str):
    return hashlib.md5(s.encode()).hexdigest()

def get_key(data: str):
    return f"{get_hash(data)}.json"    






