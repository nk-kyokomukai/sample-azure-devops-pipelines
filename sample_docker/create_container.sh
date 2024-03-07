# !/bin/bash

CURRENT=$(cd $(dirname $0);pwd)

cd $CURRENT

docker load -i azure_pipelines_sample_image.tar.gz
docker-compose up -d --build

pause