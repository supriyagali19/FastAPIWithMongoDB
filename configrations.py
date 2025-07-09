
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://supriyagali19:bwwdq629jImVxZX8@data.gqnh2e0.mongodb.net/?retryWrites=true&w=majority&appName=data"

client = MongoClient(uri, server_api=ServerApi('1'))

db= client.edb
collection = db['empdata']
