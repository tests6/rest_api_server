#!/bin/bash

# Build the Docker image
docker build -t ayomi-rest-api-server .

# Run the Docker container
docker run -d -p 8000:8000 --name ayomi-rest-api-server ayomi-rest-api-server

# Connect to the network
docker network connect ayomi-network ayomi-rest-api-server