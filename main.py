from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient, DESCENDING, ASCENDING
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

client = MongoClient('mongodb://localhost:27017/')
db = client['course_database']
collection = db['courses']

class Chapter(BaseModel):
    name: str
    text: str

class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]

@app.get("/courses", response_model=List[Course])
def get_courses(
    sort_by: str = Query("alphabetical", pattern="^(alphabetical|date|rating)$"),
    domain: Optional[str] = None
):
    sort_field = "name" if sort_by == "alphabetical" else "date" if sort_by == "date" else "ratings.total"
    sort_order = ASCENDING if sort_by == "alphabetical" else DESCENDING

    query = {}
    if domain:
        query["domain"] = domain

    courses = list(collection.find(query).sort(sort_field, sort_order))
    return courses

@app.get("/courses/{course_name}", response_model=Course)
def get_course(course_name: str):
    course = collection.find_one({"name": course_name})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.get("/courses/{course_name}/chapters/{chapter_name}", response_model=Chapter)
def get_chapter(course_name: str, chapter_name: str):
    course = collection.find_one({"name": course_name})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    for chapter in course['chapters']:
        if chapter['name'] == chapter_name:
            return chapter

    raise HTTPException(status_code=404, detail="Chapter not found")

class Rating(BaseModel):
    rating: int

@app.post("/courses/{course_name}/chapters/{chapter_name}/rate")
def rate_chapter(course_name: str, chapter_name: str, rating: Rating):
    if rating.rating not in [-1, 1]:
        raise HTTPException(status_code=422, detail="Rating must be either -1 or 1")

    result = collection.update_one(
        {"name": course_name, "chapters.name": chapter_name},
        {"$inc": {"ratings.total": rating.rating, "ratings.count": 1}}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Course or chapter not found")

    return {"message": "Rating submitted successfully"}
