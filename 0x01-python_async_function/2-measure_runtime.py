#!/usr/bin/env python3
"""
    This script measures the total execution time of wait_n(n, max_delay)
"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        measure the total execution time of wait_n(n, max_delay)
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
