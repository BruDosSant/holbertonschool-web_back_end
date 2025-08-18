#!/usr/bin/env python3


"""
Ejercicio 1 clase para paginar una base de datos
"""


import csv
import math
from typing import List


"""
Como organizar en paginas
"""


def index_range(page: int, page_size: int) -> tuple:

    """retorna tupla de inicio y fin"""

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


"""
Ejercicio 1 clase para paginar una base de datos
"""


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

        """
        Return a page of the dataset.
        """

        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
    
        """
        Return a dictionary with pagination details.
       """

    data = self.get_page(page, page_size)
    total_items = len(self.dataset())
    total_pages = math.ceil(total_items / page_size)

    return {
        'page_size': len(data),       # puede ser menor en la última página
        'page': page,
        'data': data,
        'next_page': page + 1 if page < total_pages else None,
        'prev_page': page - 1 if page > 1 else None,
        'total_pages': total_pages
    }
