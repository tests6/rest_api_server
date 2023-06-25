#!/bin/bash

# Stop the Docker container
docker stop ayomi-rest-api-server

# Remove the Docker container
docker rm ayomi-rest-api-server

# Remove the Docker image
docker rmi ayomi-rest-api-server