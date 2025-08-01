#!/usr/bin/env python3

'''funcion que lanza múltiples tareas asíncronas usando task_wait_random'''


import asyncio
from typing import List
import importlib
task_wait_random = importlib.import_module('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''ejecuta n tareas de espera aleatoria con un máximo delay especificado'''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
