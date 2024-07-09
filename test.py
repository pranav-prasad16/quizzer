from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
uri = "mongodb+srv://nanichandra:database123@test.8ia7twi.mongodb.net/?retryWrites=true&w=majority&appName=test"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['questionnoire']
collection = db['question']

correct_answers = list(collection.find({"country": country, "exam": exam}, {"_id": 0, "correct_option": 1}))

print(correct_answers)
    
