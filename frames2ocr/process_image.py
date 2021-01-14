
import numpy as np
from PIL import Image
from pytesseract import image_to_string

def read_image(path):
    return Image.open(path)

def crop_convert(img,crop=(195,1020,1500,1080)):
    return np.array(img.crop(crop).convert("L"))

def filter_image(img,cuttoff=200):
    return Image.fromarray((img > cuttoff).astype("uint8"))

def extract_text(img):
    return image_to_string(img).strip()

def process_image(path,crop=(195,1020,1500,1080),cuttoff=200):
    print("Reading image...")
    img = read_image(path)
    print("Cropping image and converting to B&W...")
    img = crop_convert(img,crop=crop)
    print("Filtering image...")
    img = filter_image(img,cuttoff=cuttoff)
    print("Performing OCR...")
    return extract_text(img)

