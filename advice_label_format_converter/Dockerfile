FROM ubuntu:20.04

LABEL maintainer="arodriguez@catec.aero"

ARG DEBIAN_FRONTEND=noninteractiva
ENV TZ=Europe/Moscow

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev
RUN apt-get install -y ffmpeg libsm6 libxext6
RUN pip3 install --upgrade pip

WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /labels
RUN mkdir /labels/coco
RUN mkdir /labels/cvat
RUN mkdir /labels/pascal
COPY labels/coco/* /labels/coco
COPY labels/cvat/* /labels/cvat
COPY labels/pascal/* /labels/pascal

COPY label_converter.py label_converter.proto LICENSE server.py classes.json ./

RUN python3 -m grpc_tools.protoc --python_out=. --proto_path=. --grpc_python_out=. *.proto

ENTRYPOINT ["python3", "-u", "server.py"]