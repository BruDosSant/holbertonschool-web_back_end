#!/usr/bin/env python3

'''funcion que espera un tiempo entre 0 y 10'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''retorna el tiempo esperado entre 0 y 10'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
