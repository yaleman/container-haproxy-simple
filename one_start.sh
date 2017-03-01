#!/bin/bash

eval $(docker-machine env default)
docker-compose restart
