# https://www.w3schools.com/python/python_mongodb_update.asp
from pymongo import MongoClient 

client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT,
                    username=MONGODB_USERNAME,
                    password=MONGODB_PASSWORD)

my_database = client["mydatabase"] 
my_collection = my_database["mycollection"] 

for doc in my_collection.find({}):
    print(doc)

my_query = {"address": "Valley 345"}
new_values = {"$set" : {"address": "Canyon 123"}}

my_collection.update_one(my_query, new_values) # Update One

for doc in my_collection.find():
    print(doc)

my_query = { "address": { "$regex": "^S" } }
new_values = { "$set": { "name": "Minnie" } }
history = my_collection.update_many(my_query, new_values)
print(history.modified_count, " documents updated.")

