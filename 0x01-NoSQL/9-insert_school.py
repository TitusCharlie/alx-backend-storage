#!/usr/bin/env python3
""" Insert a document into a collection """
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection """
    return mongo_collection.insert_one(kwargs).inserted_id