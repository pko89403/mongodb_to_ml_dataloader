# https://www.w3schools.com/python/python_mongodb_delete.asp
from pymongo import MongoClient 

client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT,
                    username=MONGODB_USERNAME,
                    password=MONGODB_PASSWORD)

dblist = client.list_database_names()

my_database = client["mydatabase"] # Creating a Database
my_collection = my_database["mycollection"] # Creating a Collection

my_query = { "_id" : "1" }
my_doc = my_collection.find(my_query)
for doc in my_doc:
    print(doc)
my_collection.delete_one(my_query) # Delete 1 Document
my_doc = my_collection.find(my_query)
for doc in my_doc:
    print(doc)

my_query = { "address": {"$regex": "^S"} }
doc = my_collection.delete_many(my_query) # Delete Many Documents
print(doc.deleted_count, " documents deleted.")

doc = my_collection.delete_many({}) # Delete All Documents
print(doc.deleted_count, " documents deleted.")

# Drop Collection ( ~= Table )
my_collection.drop()