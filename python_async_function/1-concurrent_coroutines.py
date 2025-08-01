#!/usr/bin/env python3

'''funcion que lanzar múltiples esperas en paralelo y devolver
los tiempos ordenados.'''


import asyncio
from typing import List
import importlib
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''retorna la lista con todas las esperas dentro'''
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for a in asyncio.as_completed(tasks):
        delay = await a
        delays.append(delay)

    return delays
