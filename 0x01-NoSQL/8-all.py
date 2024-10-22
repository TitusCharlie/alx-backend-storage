#!/usr/bin/env python3
""" List all documents """
from pymongo import MongoClient

def list_all(mongo_collection):
    """ Lists all documents in a collection """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())