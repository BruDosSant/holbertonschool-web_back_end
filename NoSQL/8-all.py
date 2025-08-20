#!/usr/bin/env python3


"""
modulo 8-all
"""


def list_all(mongo_collection):
    """
    Lista todos los documentos de la colección proporcionada.

    Args:
        mongo_collection: objeto Collection de pymongo.

    Returns:
        lista de diccionarios, cada uno representando un documento.
    """
    return list(mongo_collection.find())
