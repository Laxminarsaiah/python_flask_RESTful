"""mongo client"""
from pymongo import MongoClient


class MyMongoClient:
    """mongo client"""

    def __init__(self):
        self.client = MongoClient("mongodb://127.0.0.1:27017/pywebdb")

    def get_client(self):
        """mongoclient"""
        return self.client
