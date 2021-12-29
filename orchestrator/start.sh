#!/bin/bash
echo "[INFO]: Starting pipeline..."

docker stop $(docker ps -aq)

docker build -t fadacatec/advice-img-databroker:st3 $HOME/advice-local-pipeline/advice-img-databroker/
docker build -t fadacatec/advice-road-crop:st3 $HOME/advice-local-pipeline/advice-road-crop/
docker build -t fadacatec/advice-yolo:st3 $HOME/advice-local-pipeline/advice-yolo/
docker build -t fadacatec/advice-label-assistant:st3 $HOME/advice-local-pipeline/advice-lat/

docker run --detach -v $HOME/advice-local-pipeline/shared_folder:/shared_folder -p 8000:8000 fadacatec/advice-img-databroker:st3
if [[ $1 == "-r" ]]
then
    docker run --detach -p 8001:8001 fadacatec/advice-road-crop:st3
fi
docker run --detach -v $HOME/advice-local-pipeline/shared_folder:/shared_folder -p 8002:8002 fadacatec/advice-yolo:st3
docker run --detach -v $HOME/advice-local-pipeline/shared_folder:/app/shared_folder/ -p 8004:8062 -p 8003:8003 fadacatec/advice-label-assistant:st3