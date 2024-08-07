import json
from pymongo import MongoClient, ASCENDING, DESCENDING

with open('courses.json') as f:
    courses = json.load(f)

client = MongoClient('mongodb://localhost:27017/')
db = client['course_database']
collection = db['courses']

collection.drop()

collection.insert_many(courses)

collection.create_index([('name', ASCENDING)])
collection.create_index([('date', DESCENDING)])
collection.create_index([('ratings.total', DESCENDING)])

print("Courses data has been successfully added to MongoDB.")
