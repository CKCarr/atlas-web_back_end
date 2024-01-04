#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function
with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
and
returns total_time / n.
Your function should return a float.

Use the time module to measure an approximate elapsed time.
"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Function measure_time that measures the total execution time
    for wait_n(n, max_delay) and returns total_time / n
    Args:
        n (int): number of times to call wait_random
        max_delay (int): max wait time for each call to wait_random

    Returns:
        float: total_time / n
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
