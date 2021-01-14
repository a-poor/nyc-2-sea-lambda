FROM public.ecr.aws/lambda/python:3.8

COPY app.py .
COPY requirements.txt .
COPY process_image.py .

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum -y update && \
    yum -y install tesseract && \
    pip install -r requirements.txt

CMD [ "app.lambda_handler" ]

