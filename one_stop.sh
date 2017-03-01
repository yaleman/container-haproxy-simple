#!/bin/bash

eval $(docker-machine env default)
docker ps | grep containerhaproxysimple_nginx2 | tail -1 | awk '{print $1}' | xargs -I {} docker stop {}
