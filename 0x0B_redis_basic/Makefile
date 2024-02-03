# Description: Makefile for the Redis basic project.
# This Makefile is used to manage Docker containers and images for development and testing.
# This Makefile is used to build, run, execute, stop, and clean the Docker container.
# Created by: CKCarr
# Created on: 02/02/2024

# Default action if no target is specified
# make - will execute the build target
.DEFAULT_GOAL := build

# Docker image variables for container names and directories
# The HOST_DIRECTORY is the current directory
# the CONTAINER_DIRECTORY is the directory inside the Docker container
DOCKER_IMAGE_NAME = redis_basic
DOCKER_CONTAINER_NAME = redis_basic_container
HOST_DIRECTORY=./
CONTAINER_DIRECTORY=/0x0B_redis_basic
.PHONY: build run run-interactive exec stop clean

# Build the Docker image in the current directory
build:
	@echo "Building the Docker image..."
	docker build -t $(DOCKER_IMAGE_NAME) .

# Run the Docker container in the background "-d" -detached
#  with the current directory mounted to the container directory
run:
	@echo "Running the Docker container in the background..."
	docker run -d --name $(DOCKER_CONTAINER_NAME) -v ${HOST_DIRECTORY}:${CONTAINER_DIRECTORY} ${DOCKER_IMAGE_NAME}

# Run the Docker container in interactive mode with a bash shell
run-interactive:
	@echo "Running the Docker container interactively..."
	docker run -it --name $(DOCKER_CONTAINER_NAME) -v ${HOST_DIRECTORY}:${CONTAINER_DIRECTORY} $(DOCKER_IMAGE_NAME) /bin/bash

# Execute a bash shell in the Docker container for debugging purposes
# allows for running commands inside the container
exec:
	@echo "Executing a bash shell inside the Docker container..."
	docker exec -it $(DOCKER_CONTAINER_NAME) bash

# Stop running Docker container and remove it
# This frees up resources
stop:
	@echo "Stopping and removing the Docker container..."
	docker stop $(DOCKER_CONTAINER_NAME)
	docker rm $(DOCKER_CONTAINER_NAME)

# Clean up Docker container and image
# This is useful for removing all traces of the Docker container
# and image from the system
clean:
	@echo "Cleaning up the Docker container and image..."
	docker stop $(DOCKER_CONTAINER_NAME) || true
	docker rm $(DOCKER_CONTAINER_NAME) || true
	docker rmi $(DOCKER_IMAGE_NAME) || true
