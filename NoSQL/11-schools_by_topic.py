#!/usr/bin/env python3


"""
modulo 8-all
"""


def schools_by_topic(mongo_collection, topic):
    """
    lista de escuelas por topic
    """

    lista = mongo_collection.find({topics: topic})
    return lista