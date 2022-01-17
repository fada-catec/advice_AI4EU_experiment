docker stop $(docker ps -aq)

docker build -t advice-img-databroker .
docker run -v /home/arodriguez/advice-local-pipeline/shared_folder:/shared_folder -p 8000:8000 advice-img-databroker