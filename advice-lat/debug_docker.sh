#!/bin/bash
echo "[INFO]: Reloading docker container..."
docker stop $(docker ps -aq)
docker build -t advice-label-assistant .
docker run -v /home/arodriguez/advice-local-pipeline/shared_folder:/app/shared_folder/ -p 8004:8062 -p 8003:8003 advice-label-assistant


