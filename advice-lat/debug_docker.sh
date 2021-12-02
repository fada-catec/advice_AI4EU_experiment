#!/bin/bash
echo "[INFO]: Reloading docker container..."
docker stop $(docker ps -aq)
docker build -t advice-label-assistant .
docker run -v /home/lfernandez/arodriguez_ws/advice_dockers/advice-lat-local/shared_folder/new_labels:/app/shared_folder/new_labels -p 8004:8062 -p 8061:8061 advice-label-assistant


