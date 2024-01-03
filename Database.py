from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId
from config import config


class Database(object):
    def __init__(self):
        self.client = MongoClient(config['db']['url'],
                        username=config['db']['user'],
                        password=config['db']['password'])
        self.db = self.client[config['db']['name']]

    def insert(self, element, collection_name):
        inserted = self.db[collection_name].insert_one(element)
        return str(inserted.inserted_id)

    def find(self, criteria, collection_name, projection=None, sort=None, limit=0, cursor=False):  # find all from db

        found = self.db[collection_name].find(filter=criteria, projection=projection, limit=limit, sort=sort)

        if cursor:
            return found

        found = list(found)

        for i in range(len(found)):  # to serialize object id need to convert string
            if "_id" in found[i]:
                found[i]["_id"] = str(found[i]["_id"])

        return found