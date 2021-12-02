#!/bin/bash
echo "[INFO]: Reloading docker container..."
docker stop $(docker ps -aq)
docker build -t advice-yolo .
docker run -p 8061:8061 advice-yolo