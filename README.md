# NYC-2-SEA: Lambda

_created by Ausitn Poor_

Using AWS Lambda functions to process videos as they're uploaded to
S3 buckets.

Roadtrip videos are uploaded to an S3 bucket (`s3://nyc2sea-rawvideo`), 
triggering the Lambda function in [vid2frames](./vid2frames), which 
converts the videos to images and stores them into a new bucket 
(`s3://nyc2sea-rawimages`).

A second Lambda function, in [frames2ocr](./frames2ocr),  watches 
`s3://nyc2sea-rawimages` for new frames. When new frames get added, this 
function uses PyTesseract to perform OCR on the image (after a bit of 
preprocessing) and then saves the results (as a JSON file) to a third 
S3 bucket (`s3://nyc2sea-ocrdata`).

There are makefiles included for simplifying the process of building,
tagging and pushing the Lambda function docker images to AWS ECR.

