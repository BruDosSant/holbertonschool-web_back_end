#!/usr/bin/env python3

'''funcion que genera 10 números aleatorios entre 0 y 10
con una pausa de 1 segundo.'''


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''genera 10 números aleatorios entre 0 y 10
    con una pausa de 1 segundo.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
