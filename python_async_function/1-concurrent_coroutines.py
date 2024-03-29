#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async

Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order
without using sort() because of concurrency.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function wait_n that takes in 2 int arguments
    (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.

    Args:
        n (int): random number of times to spawn wait_random
        max_delay (int): max delay to wait_random

    Returns:
        List[float]: list of all delays in ascending order may be float values
    """
    # if the given n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # otherwise create a delay list
    delays_list = []

    # create a list of tasks to run concurrently
    tasks = [wait_random(max_delay) for i in range(n)]

    # run the tasks concurrently
    for task in asyncio.as_completed(tasks):
        # await each task and append the result to the delays_list
        delays_list.append(await task)

    return delays_list
