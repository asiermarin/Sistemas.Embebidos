# delete the old image and create a new one
docker rmi mysql-image-service
docker build -f Dockerfile-Mysql -t mysql-image-service .

