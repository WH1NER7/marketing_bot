from pymongo import MongoClient

try:
    conn = MongoClient()
    db = conn["myk_bot"]
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")
