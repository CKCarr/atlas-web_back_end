# Use Ubuntu 18.04 as the base image
FROM ubuntu:18.04

# Set noninteractive to avoid tzdata hanging
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

# Install wget and gnupg before adding MongoDB GPG key
RUN apt-get update && \
    apt-get install -y wget gnupg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install MongoDB
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list && \
    apt-get update && \
    apt-get install -y tzdata mongodb-org && \
    mkdir -p /data/db && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install essential tools and Python build dependencies
RUN apt-get update && \
    apt-get install -y curl wget git tar vim emacs build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev locales && \
    locale-gen en_US.UTF-8

# Install Python 3.7 from source
RUN cd /usr/src && \
    wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz && \
    tar -xf Python-3.7.3.tar.xz && \
    cd Python-3.7.3 && \
    ./configure && \
    make altinstall

# Create a symbolic link for Python 3.7 to be recognized as 'python3'
# This is the new line added to ensure 'python3' command is available
RUN ln -s /usr/local/bin/python3.7 /usr/bin/python3 && \
    python3 --version # Verify Python installation

# Update pip and install Python packages from requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN ln -s /usr/local/bin/pip3.7 /usr/bin/pip && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Add MongoDB init script
ADD init.d-mongod /etc/init.d/mongod
RUN chmod u+x /etc/init.d/mongod

# Create a test user
RUN useradd -M correction_tester

# Set the locale
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Copy the entrypoint script to the container
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Set the entrypoint script to be executed
ENTRYPOINT ["/start.sh"]
