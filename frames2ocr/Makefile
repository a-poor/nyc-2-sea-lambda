help:
	@echo "OPTIONS: build, login, tag, push, all"

all: build login tag push

build:
	docker build -t nyc2sea-lambda-frames2ocr .
login:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 580367176505.dkr.ecr.us-east-1.amazonaws.com

tag:
	docker tag nyc2sea-lambda-frames2ocr:latest 580367176505.dkr.ecr.us-east-1.amazonaws.com/nyc2sea-lambda-frames2ocr:latest

push:
	docker push 580367176505.dkr.ecr.us-east-1.amazonaws.com/nyc2sea-lambda-frames2ocr:latest

