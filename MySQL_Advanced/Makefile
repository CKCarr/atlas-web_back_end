# Description: Makefile for the Redis basic project.
# This Makefile is used to manage Docker containers and images for development and testing.
# This Makefile is used to
# build run run-interactive exec-cmd stop clean the Docker container.
# Created by: CKCarr
# Created on: 02/02/2024

# Color definitions
RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[1;33m
NC=\033[0m # No Color

# Default action if no target is specified
# make - will execute the build target
.DEFAULT_GOAL := build

# Docker image variables for container names and directories
# The HOST_DIRECTORY is the current directory
# the CONTAINER_DIRECTORY is the directory inside the Docker container
DOCKER_IMAGE_NAME = mysql_advanced
DOCKER_CONTAINER_NAME = mysql_advanced_container
HOST_DIRECTORY=./
CONTAINER_DIRECTORY=/mysql_advanced
.PHONY: build run run-interactive exec-cmd stop clean

# Build the Docker image in the current directory
build:
	@echo "${GREEN}Building the Docker image...${NC}"
	docker build -t $(DOCKER_IMAGE_NAME) .

# Run the Docker container in the background "-d" -detached
#  with the current directory mounted to the container directory
run:
	@echo "${GREEN}Running the Docker container in the background...${NC}"
	docker run -d --name $(DOCKER_CONTAINER_NAME) -v ${HOST_DIRECTORY}:${CONTAINER_DIRECTORY} ${DOCKER_IMAGE_NAME}

# Run the Docker container in interactive mode with a bash shell
# This is useful for debugging and running commands inside the container
run-interactive:
	@echo "${GREEN}Running the Docker container interactively...${NC}"
	@echo "${YELLOW}Type 'exit' to stop the container and return to the host shell.${NC}"
	docker run -it --name $(DOCKER_CONTAINER_NAME) -v ${HOST_DIRECTORY}:${CONTAINER_DIRECTORY} $(DOCKER_IMAGE_NAME) /bin/bash

# Execute a bash shell in the Docker container for debugging purposes
# allows for running commands inside the container
# Example: make exec-cmd CMD="ls -l" - will execute "ls -l" inside the container
CMD ?= "bash"

exec-cmd:
	@echo "${YELLOW}Executing a bash shell inside the Docker container...$(NC)"
	docker exec -it $(DOCKER_CONTAINER_NAME) /bin/bash -c $(CMD)

# Stop running Docker container and remove it
# This frees up resources
stop:
	@echo "${RED}Stopping and removing the Docker container...${NC}"
	docker stop $(DOCKER_CONTAINER_NAME)
	docker rm $(DOCKER_CONTAINER_NAME)

# Clean up Docker container and image
# This is useful for removing all traces of the Docker container
# and image from the system
clean:
	@echo "${RED}Cleaning up the Docker container and image...${NC}"
	docker stop $(DOCKER_CONTAINER_NAME) || true
	docker rm $(DOCKER_CONTAINER_NAME) || true
	docker rmi $(DOCKER_IMAGE_NAME) || true
