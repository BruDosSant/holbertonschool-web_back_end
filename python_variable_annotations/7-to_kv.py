#!/usr/bin/env python3

'''funcion que retorna una tupla con un string y un float'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''retorna una tupla con el string k y el cuadrado de v como float.'''
    return (k, float(v ** 2))
