#!/usr/bin/env python3
""" async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ async coroutine """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
