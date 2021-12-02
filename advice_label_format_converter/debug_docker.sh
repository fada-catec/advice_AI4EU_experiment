#!/bin/bash
echo "[INFO]: Reloading docker container..."
docker stop $(docker ps -aq)
docker build -t advice-label-converter .
docker run -v /home/lfernandez/arodriguez_ws/advice_dockers/advice_label_format_converter/shared_folder/:/shared_folder/ -p 8061:8061 advice-label-converter