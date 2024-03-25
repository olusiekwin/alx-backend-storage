#!/usr/bin/env python3
""" module for the function list_all """


def list_all(mongo_collection):
    """a Python function that lists all documents in a collection"""
    return mongo_collection.find()
