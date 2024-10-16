#!/usr/bin/env python3
"""
a coroutine that takes no argumets, loops 10 times,
asynchronously waits 1 second then yields a random number between 0 and 10
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times, asynchronously waits 1 second,
    then yields a number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
