#!/usr/bin/env python3

'''funcion que retorna la suma de todos los números
    en la lista que contiene ints y floats.'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Suma todos los elementos que pueden ser int o float
    y retorna un float.'''
    return float(sum(mxd_lst))
