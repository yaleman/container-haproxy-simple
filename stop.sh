#!/bin/bash

eval $(docker-machine env)
docker-compose stop
docker-compose rm -f
