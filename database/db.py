from pymongo import MongoClient
client=""


def initialize_db():
    global client 
    client= MongoClient("mongodb://localhost:27017/")
    client["videodigest"]
    return


def db_exit():
    client.close()
