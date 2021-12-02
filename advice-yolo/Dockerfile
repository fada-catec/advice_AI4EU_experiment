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

RUN mkdir /config
COPY ./config/classes.json ./config/
COPY ./config/yolo-obj_best.weights ./config/
COPY ./config/yolo-obj.cfg ./config/

COPY detection.py yolo.proto LICENSE server.py ./

RUN python3 -m grpc_tools.protoc --python_out=. --proto_path=. --grpc_python_out=. *.proto

ENTRYPOINT ["python3", "-u", "server.py"]


##Para mostrar imagenes por pantalla
# xhost +
# docker run -it --net=host --env=DISPLAY --volume=$HOME/.Xauthority:/root/.Xauthority docker-test
