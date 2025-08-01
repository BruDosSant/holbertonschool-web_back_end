#!/usr/bin/env python3

'''funcion que retorna una lista de tuplas con cada string y su longitud.'''


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''retorna una lista de tuplas con cada string y su longitud.'''
    return [(i, len(i)) for i in lst]
