#!/bin/bash

eval $(docker-machine env)
docker-compose up -d
