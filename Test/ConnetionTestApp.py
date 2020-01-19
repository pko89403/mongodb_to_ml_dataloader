# 접속 가능한지 테스트 하기 위한 간단한 Python Flask App 코드
# https://basketdeveloper.tistory.com/34
from flask import Flask 
from pymongo import MongoClient 

NLP_GPU_SERVER_HOST = 'HOST'
MONGODB_PORT = 'PORT
app = Flask(__name__)
client = MongoClient(host=NLP_GPU_SERVER_HOST,
                    port=27017)

db = client['test']

print(db)

app.run(host='0.0.0.0', port=5000)