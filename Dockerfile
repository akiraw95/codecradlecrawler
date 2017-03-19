FROM ubuntu:16.04

#to build this dockerfile first ensure that it is named "Dockerfile"
#make sure that  the file "stackoverflow_crawler.py" is also present in the same directory as "Dockerfile"
#docker build -t {YOUR DOCKERHUB USERNAME}/bs4container:0.1.1 .
#$docker run -v ~/sospider/questions:/sospider/questions/ akiraw95/bs4container:0.1.1

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
		python3-dev \
		python3-pip \
		libxml2-dev \
		libxslt1-dev \
		zlib1g-dev \
		libffi-dev \
		libssl-dev \
		nano
RUN pip3 install bs4

#ENV SCRAPYPROJ /scrapy
#ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "/sospider/questions"
WORKDIR "/sospider/"

ADD stackoverflow_crawler.py /sospider/

CMD python3 stackoverflow_crawler.py

