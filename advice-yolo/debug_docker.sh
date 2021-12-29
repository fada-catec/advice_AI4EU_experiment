#!/bin/bash
echo "[INFO]: Reloading docker container..."
docker stop $(docker ps -aq)
docker build -t advice-yolo .
# xhost +
# docker run -it --net=host --env=DISPLAY --volume=$HOME/.Xauthority:/root/.Xauthority -p 8061:8061 advice-yolo #DISPLAY IMAGES
docker run -v /home/arodriguez/advice-local-pipeline/shared_folder:/shared_folder -p 8002:8002 advice-yolo