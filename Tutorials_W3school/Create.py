# https://www.w3schools.com/python/python_mongodb_create_db.asp
from pymongo import MongoClient 


client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT,
                    username=MONGODB_USERNAME,
                    password=MONGODB_PASSWORD)

dblist = client.list_database_names()
print(f'MongoDB DataBase List : {dblist}')

my_database = client["mydatabase"] # Creating a Database
my_collection = my_database["mycollection"] # Creating a Collection


"""
new_dblist = client.list_database_names()
new_colelction = my_database.list_collection_names()
print(f'MongoDB DataBase List : {new_dblist}')
print(f'MongoDB DataBase Collection List : {new_colelction}')


my_dictionary = {"name" : "John", "address":"Highway 37"}
insert_history = my_collection.insert_one(my_dictionary) # insert one data
print(insert_history.inserted_id)

my_dict_list = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]

insert_history = my_collection.insert_many(my_dict_list) # insert many data
print(insert_history.inserted_ids)
"""
my_dict_with_id_list = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

insert_history = my_collection.insert_many(my_dict_with_id_list) # insert many data with ids
print(insert_history.inserted_ids)

client.close()