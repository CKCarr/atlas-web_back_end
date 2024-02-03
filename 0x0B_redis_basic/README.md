# Redis Basic - A Guide to Basic Operations and Caching with Redis

"Redis Basic" is an introductory project designed to equip beginners with the knowledge and skills needed to utilize Redis for basic operations and simple caching mechanisms. This project offers a structured learning path with practical tasks and clear objectives.

## Overview
Redis, short for Remote Dictionary Server, is an in-memory data structure store, used as a database, cache, and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, and geospatial indexes with radius queries. This guide will take you through setting up Redis, performing basic operations, understanding its data types, and using it as a simple cache.

<hr>

 ## Resources

Before diving into the tasks, it's recommended to go through the following resources to gain a solid understanding of Redis and its applications:

[Redis commands documentation](https://redis.io/commands/)

[Redis Python client documentation.](https://redis-py.readthedocs.io/en/stable/)

["How to Use Redis With Python" - A comprehensive guide.](https://realpython.com/python-redis/)

["Redis Crash Course Tutorial" - A quick and informative tutorial.](https://www.youtube.com/watch?v=Hbt56gFj998&ab_channel=TraversyMedia)

# Learning Objectives
Upon completion of this project, you'll learn how to:

Use Redis for basic operations like setting and getting key-value pairs.
Leverage Redis as a simple cache to enhance the performance of your applications.

# Requirements
To ensure a smooth learning experience, adhere to the following requirements:

All files must be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
Each file should end with a new line.
A README.md file, at the root of the project folder, is mandatory.
The first line of all your files should be exactly #!/usr/bin/env python3.
Your code should adhere to the pycodestyle (version 2.5).
All modules, classes, and functions/methods must have documentation.
All functions and coroutines must be type-annotated.

## Setup
Before starting, ensure Redis is installed and configured on your Ubuntu 18.04 system:

``` bash

$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
### Using Redis in a Container
Note that the Redis server is stopped by default. When starting a container, initiate it with
`service redis-server start`

# Tasks

### Task 0: Writing Strings to Redis
Create a Cache class with methods to store data in Redis and retrieve a unique key for each entry.

### Task 1: Reading from Redis and Recovering Original Type
Enhance the Cache class to convert data back to its original format when retrieved from Redis.

### Task 2: Incrementing Values
Implement a method to track and increment the number of times methods in the Cache class are called.

### Task 3: Storing Lists
Introduce a decorator to store the history of inputs and outputs for each function call in Redis lists.

### Task 4: Retrieving Lists
Develop a replay function to display the history of calls for a particular function, showcasing both the inputs and the outputs.

# Basic Operations
Redis operates primarily as a key-value store. Here are some basic operations:

- Setting a value:

``` bash

SET key value
```
This command sets the 'key' to hold the 'value'. If 'key' already holds a value, it is overwritten.

- Getting a value:
``` bash

GET key
```
This command gets the value of 'key'. If the key does not exist, nil is returned.

- Deleting a key:

```bash
DEL key
```
This command removes the specified key. If the key does not exist, it does nothing.

#  Data Types
Redis supports more than just strings; it also supports lists, sets, sorted sets, hashes, and more. Understanding these types is crucial for using Redis effectively.

- Lists: Collections of string elements sorted according to the order of insertion. They are essentially linked lists, which means that you can perform push and pop operations at both ends of the list in constant time.

``` bash

LPUSH mylist value # push value at the head
RPUSH mylist value # push value at the tail
LRANGE mylist 0 -1 # get all the elements
```
- Hashes: Maps between string fields and string values, so they are the perfect data type to represent objects.
``` bash

HSET myhash field value
HGET myhash field
```
- Sets: Collections of unique, unsorted string elements. Useful for storing unique elements.

```bash

SADD myset value
SMEMBERS myset
```
# Using Redis as a Cache
Redis is often used as a caching layer to speed up applications by storing precomputed results that are expensive to fetch or compute.

- Setting a cache with expiration:

``` bash
SETEX key seconds value
```
This command sets the 'key' to hold the 'value' and set 'key' to timeout after a given number of seconds.

- Cache invalidation: It's crucial to invalidate cache properly to avoid serving stale data. Redis provides various strategies for this, like setting an expiration time or using the DEL command to remove keys when the underlying data changes.

# Persistence and Performance
While Redis is an in-memory database, it offers options to persist data on disk. You might also want to look into:

- Snapshotting: Periodically saving the dataset to disk.
- Append-only file (AOF): Logging every write operation received by the server, to be replayed at server startup, reconstructing the original dataset.

# Client Libraries
Redis has support for many programming languages. Here are steps for Python:

- Install the redis package:
```bash

pip install redis
```
Connect and interact with Redis:
``` python

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
value = r.get('foo')
print(value)  # Output: b'bar'
```
