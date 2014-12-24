FROM ubuntu:14.04

MAINTAINER Kit Barnes <kit@ninjalith.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python3-pip git python3-dev python3-zmq
RUN pip3 install --upgrade chardet

COPY . /opt/hfb
RUN pip3 install -e /opt/hfb

ENTRYPOINT ["hfb"]
CMD []
