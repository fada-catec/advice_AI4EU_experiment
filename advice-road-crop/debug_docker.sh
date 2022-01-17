#!/bin/bash
echo "[INFO]: Reloading docker container..."
docker stop $(docker ps -aq)
docker build -t fadacatec/advice-road-crop:st3 .
docker run -p 8001:8001 fadacatec/advice-road-crop:st3 --rm –it /bin/bash