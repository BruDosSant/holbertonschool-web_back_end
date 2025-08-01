#!/usr/bin/env python3

'''funcion que retorna la multiplicacion de un float por otro float.'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''retorna una función que multiplica un float por
    el multiplicador dado.'''
    def multiplier_function(float: float) -> float:
        return float * multiplier
    return multiplier_function
