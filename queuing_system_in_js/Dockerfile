FROM ubuntu:18.04

RUN apt-get update && apt-get -y upgrade

# Install essential packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    vim \
    emacs \
    locales \
    build-essential \
    gcc

# Set locale
RUN locale-gen en_US.UTF-8

# Set environment variables for the locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Setup Node.js
RUN curl -sl https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get update && apt-get install -y nodejs

# Install Redis server and client
RUN apt-get -y install redis-server
RUN sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

# Install project dependencies
RUN mkdir /tmp/node_packages
COPY package.json /tmp/node_packages/package.json
RUN cd /tmp/node_packages && npm install

# Create and switch to a non-root user
RUN useradd -m correction_tester

# Expose ports
EXPOSE 3000 6379

# Make the start script executable
COPY start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
