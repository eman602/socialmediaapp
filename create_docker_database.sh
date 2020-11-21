#!/bin/bash

curl https://get.docker.com | sudo bash

sudo usermod -aG docker $(whoami) 

docker network create socialnetwork

docker volume create socialvolume

export SOCIALAPP_URI=mysql+pymysql://root:1234@127.0.0.1:3306/socialdb SECRET_KEY=sdcsdcsdcsc

docker run -d -p 3306:3306 --network socialnetwork -v socialvolume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=socialdb --name mysql mysql:5.7 