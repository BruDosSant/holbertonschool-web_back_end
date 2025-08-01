#!/usr/bin/env python3

'''funcion recopila 10 números aleatorios desde async_generator.'''


from typing import List
import asyncio
import importlib
from typing import Generator
async_generator = importlib.import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''recopila 10 números aleatorios desde async_generator.'''
    return [n async for n in async_generator()]
