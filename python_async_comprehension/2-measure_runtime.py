#!/usr/bin/env python3

"""funcion que mide el tiempo que tarda en ejecutarse
async_comprehension 4 veces en paralelo."""

import asyncio
import time
import importlib
async_comprehension = (
    importlib.import_module('1-async_comprehension').async_comprehension
)


async def measure_runtime() -> float:
    '''ejecuta async_comprehension 4 veces en paralelo
    y mide el tiempo total.'''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    total = end - start
    return total
