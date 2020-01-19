# pymongo.errors.BulkWriteError: batch op errors occurred
# CSV 파일을 MongoDB로 벌크 업데이트 하기 
# 키 값 중복 나서 에러 터졌었음 ...
# BulkWriteError

import csv
import json
from pymongo import MongoClient 
import pandas as pd;
from pymongo.errors import BulkWriteError

def csv_to_json(filename):
    data = pd.read_csv(filename)
    data.drop(columns=['id'], inplace=True)
    data['_id'] = data.index 
    return data.to_dict('records')

client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT,
                    username=MONGODB_USERNAME,
                    password=MONGODB_PASSWORD)

database = client["NLP"] # Creating a Database
collection = database["google_api"] # Creating a Collection

try:
    history = collection.insert_many(csv_to_json(CSV_FILENAME))
except BulkWriteError as bwe:
    for err in bwe.details['writeErrors']:
        if int(err['code']) == 11000:
            print("Duplicate Key, Don't Care")
        else:
            print(err['errmsg']) 