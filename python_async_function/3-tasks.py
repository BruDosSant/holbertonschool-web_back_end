#!/usr/bin/env python3

'''funcion que retorna una asyncio.Task que ejecuta wait_random'''


import asyncio
import time
import importlib
wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''crea y retorna una asyncio.Task que ejecuta wait_random'''
    return asyncio.create_task(wait_random(max_delay))
