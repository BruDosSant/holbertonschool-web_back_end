#!/usr/bin/env python3


"""
modulo 8-all
"""


def update_topics(mongo_collection, name, topics):
    """
    inserta documento en coleccion
    """

    documento = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return documento