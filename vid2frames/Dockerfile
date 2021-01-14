FROM public.ecr.aws/lambda/python:3.8

COPY app.py .
COPY requirements.txt .

RUN yum -y update && \
    yum -y upgrade && \
    yum -y install opencv opencv-devel opencv-python && \
    pip install -r requirements.txt

CMD [ "app.lambda_handler" ]
