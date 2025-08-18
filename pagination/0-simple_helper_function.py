#!/usr/bin/env python3


"""
Como organizar en paginas
"""


def index_range(page: int, page_size: int) -> tuple:

    """retorna tupla de inicio y fin"""
    
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
