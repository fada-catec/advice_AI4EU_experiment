docker stop $(docker ps -aq)

docker build -t advice-img-databroker .
docker run -v /home/lfernandez/arodriguez_ws/advice_dockers/advice-img-databroker/shared_folder:/shared_folder -p 8061:8061 advice-img-databroker