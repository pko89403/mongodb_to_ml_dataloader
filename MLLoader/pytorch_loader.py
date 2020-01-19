import io
import os
import numpy as np 
from pymongo import MongoClient
from torch.utils.data import Dataset, DataLoader 

MONGODB_HOST = 'IP'
MONGODB_PORT = 'PORT'
MONGODB_USERNAME = 'USERNAME'
MONGODB_PASSWORD = 'PASSWORD'

class DatasetDB(Dataset):
    def __init__(self, db_name='NLP', 
                col_name='google_api', 
                input_list=['source_review_content', 'translatedText'], 
                label_list=['detectedSourceLanguage'], 
                transform=None):
        self.transform = transform
        self.input_list = input_list
        self.label_name = label_list[0]

        client = MongoClient(host=MONGODB_HOST,
                    port=MONGODB_PORT,
                    username=MONGODB_USERNAME,
                    password=MONGODB_PASSWORD)
        db = client[db_name]
        self.col = db[col_name]
        self.examples = list(self.col.find({}))
        self.labels = self.get_labels()
        print(self.labels)

    def __len__(self):
        return len(self.examples)

    def get_labels(self):
        category_ids = [e[self.label_name] for e in self.examples]
        return {cid: i for i , cid in enumerate(sorted(list(set(category_ids))))}

    def __getitem__(self, i):
        _id = self.examples[i]['_id']
        doc = self.col.find_one({'_id' : _id})

        #input = doc['source_review_content']
        input = tuple(doc[d] for d in self.input_list)

        if self.transform is not None:
            input = self.transform(x)

        
        label = self.labels[doc[self.label_name]]
        return input, label, _id

if __name__ == "__main__":
    dataset = DatasetDB()
    loader = DataLoader(dataset, batch_size=1, shuffle=False, num_workers=2)
    for input, label, prod in loader:
        print('input - ', input)
        print('label - ', label.item())
        print('prod - ', prod.item())