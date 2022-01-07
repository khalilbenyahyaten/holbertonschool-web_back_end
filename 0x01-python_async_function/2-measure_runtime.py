#!/usr/bin/env python3
""" measure time func """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure time func """
    time_to_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_finish = (time.time() - time_to_start)
    return time_finish / n