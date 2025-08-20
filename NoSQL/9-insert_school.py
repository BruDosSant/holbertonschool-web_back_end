#!/usr/bin/env python3


"""
modulo 8-all
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserta documento en coleccion
    """

    documento = mongo_collection.insert_one(kwargs)
    return documento.inserted_id