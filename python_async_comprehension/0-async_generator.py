#!/usr/bin/env python3
"""
0. Async Generator

Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
Use the random module.
"""
import asyncio
import random


async def async_generator():
    """
    Function async_generator coroutine that will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.

    :param None: None
    :return: 10 random numbers between 0 and 10 - may be float
    """
    for _ in range(10):
        # wait asynchronously for 1 second
        await asyncio.sleep(1)
        # yield a random number between 0 and 10
        yield random.randint(0, 10)
