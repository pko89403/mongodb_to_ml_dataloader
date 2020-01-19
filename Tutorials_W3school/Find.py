# https://www.w3schools.com/python/python_mongodb_find.asp

from pymongo import MongoClient 

client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT,
                    username=MONGODB_USERNAME,
                    password=MONGODB_PASSWORD)
my_database = client["mydatabase"] # Creating a Database
my_collection = my_database["mycollection"] # Creating a Collection

# Find All
for doc in my_collection.find():
    print( doc )

# Find Only Some Fields
for doc in my_collection.find({}, { "_id" : 0, "name" : 1, "address": 1 }):
    print( doc )     

for doc in my_collection.find({}, { "_id" : 0}):
    print( doc )     

# Query
my_query = { "address" : "Park Lane 38"}
my_document = my_collection.find(my_query)

for doc in my_document:
    print( doc )

# Advanced Query
my_advanced_query = {"address" : { "$gt": "S"} } # address field starts with the letter "S"
my_document = my_collection.find(my_advanced_query)
for doc in my_document:
    print( doc )

# REX Filter
my_advanced_query = {"address" : { "$regex": "^S"} } # address field starts with the letter "S"
my_document = my_collection.find(my_advanced_query)
for doc in my_document:
    print( doc )

# Sort
my_document = my_collection.find().sort("name", -1 ) # Descending Order
for doc in my_document:
    print( doc )