# !/bin/bash

CURRENT=$(cd $(dirname $0);pwd)

cd $CURRENT

sudo docker load -i azure_pipelines_sample_image.tar.gz
sudo docker-compose up -d --build

pause