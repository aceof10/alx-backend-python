#!/usr/bin/env python3
"""
an asyncronous coroutine that takes in an interger arg,
waits for a random delay, and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and
    and return the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
