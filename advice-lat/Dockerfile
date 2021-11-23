# debian with Python preinstalled
FROM python:3.7-slim-buster

# copy dependency information
COPY requirements.txt /

# install Python packages
RUN /usr/local/bin/python -m pip install --upgrade pip\
    && apt-get update -y\
    && apt-get install -y ffmpeg libsm6 libxext6\
    && pip install -r /requirements.txt

# copy sources
RUN mkdir /app
RUN mkdir /app/templates
RUN mkdir /app/shared_folder
RUN mkdir /app/shared_folder/img
RUN mkdir /app/shared_folder/orig_labels
RUN mkdir /app/shared_folder/new_labels
RUN mkdir /app/res

COPY gui.css gui.js label.proto server.py /app/
COPY templates/* /app/templates/
COPY res/* /app/res/
COPY shared_folder/img/* /app/shared_folder/img/
COPY shared_folder/orig_labels/* /app/shared_folder/orig_labels/
COPY shared_folder/* /app/shared_folder/

# adhere to container specification by also providing these two files
COPY label.proto /model.proto
COPY LICENSE /LICENSE

WORKDIR /app

# compile protobuf
RUN python3 -m grpc_tools.protoc --python_out=. --proto_path=. --grpc_python_out=. *.proto

EXPOSE 8061 8062

# run server with default Python log level "debug"
CMD uvicorn server:app --host 0.0.0.0 --port 8062 --log-level ${PYTHON_LOGLEVEL:-debug}
