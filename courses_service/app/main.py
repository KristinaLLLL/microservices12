from app import course
from fastapi import FastAPI, HTTPException

courses: list[course.Course] = [
    course.Course(0, 'Mathematics', [
        [0, 'Mathematical analysis', 'Text...................................'],
        [1, 'Mathematical logic', 'Text...................................'],
        [2, 'Linear algebra', 'Text...................................']]),
    course.Course(1, 'Programming', [
        [3, 'Java', 'Text...................................'],
        [4, 'Python', 'Text...................................'],
        [5, 'C++', 'Text...................................']])
]

app = FastAPI()


@app.get("/v2/courses")
def get_courses():
    return courses


@app.get("/v2/courses/{title}")
def get_course_by_title(title: str):
    info = [item for item in courses if item.title == title]
    if len(info) > 0:
        return info[0]
    return HTTPException(status_code=404, detail="Courses not found!")
