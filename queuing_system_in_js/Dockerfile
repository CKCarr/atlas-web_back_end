FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y upgrade
# curl/wget/git
RUN apt-get install -y curl wget git tar
# vim/emacs
RUN apt-get install -y vim emacs

# Set locale
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Setup Node
RUN curl -sl https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh \
    && bash nodesource_setup.sh \
    && apt-get update && apt-get install -y nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install redis server and the redis client
# Install Redis
RUN apt-get update && apt-get install -y redis-server && \
    sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

COPY package.json ./
RUN npm install

# Create test user
RUN useradd -M correction_tester

# Copy the start script
COPY start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]
