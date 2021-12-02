FROM ubuntu:18.04

LABEL maintainer=rluque@catec.aero

RUN apt-get update -y 
RUN apt-get install -y python3-pip python3-dev 
RUN pip3 install --upgrade pip

RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN python3 -m pip install tensorflow-gpu==1.14.0
RUN python3 -m pip install scikit-build
RUN python3 -m pip install matplotlib==3.1.1
RUN python3 -m pip install h5py==2.10.0
RUN python3 -m pip install keras==2.3.1
RUN python3 -m pip install segmentation-models
RUN python3 -m pip install albumentations==0.4.5
RUN python3 -m pip install opencv-python==3.4.2.17
RUN python3 -m pip install pytest

RUN python3 -m pip install numpy
RUN python3 -m pip install Pillow

WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

# RUN useradd app
# USER app
RUN mkdir /imgs
COPY ./imgs/test_img.jpg ./imgs/

# RUN mkdir /src
# COPY ./src/ ./src/ 

COPY . /

RUN python3 -m grpc_tools.protoc --python_out=. --proto_path=. --grpc_python_out=. *.proto

ENTRYPOINT [ "python3","-u","server.py" ]
# CMD python3 csv_server.py
# ENTRYPOINT ["/bin/bash", "-c", "--"]