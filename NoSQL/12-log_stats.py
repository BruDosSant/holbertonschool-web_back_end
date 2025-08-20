#!/usr/bin/env python3


"""
modulo 8-all
"""


from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient()

    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    print(f"\tmethod GET: {collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {collection.count_documents({'method': 'DELETE'})}")

    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check")