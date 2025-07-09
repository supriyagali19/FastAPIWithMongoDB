
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "replace with your connection string"

client = MongoClient(uri, server_api=ServerApi('1'))

db= client.edb
collection = db['empdata']
