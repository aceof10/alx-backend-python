#!/usr/bin/env python3
"""
contains a coroutine uses async comprehensiions to collect random
numbers from an asynchronous generator.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine that collects 10 random numbers using an async
    comprehension over async_generator
    """
    return [i async for i in async_generator()]
