from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = [
    {"rollno":1,"name":"John","age":20,},
    {"rollno":2,"name":"Jane","age":21,},
    {"rollno":3,"name":"Bob","age":22,},
]

class Student(BaseModel):
    rollno: int
    name: str
    age: int

@app.get("/")
def home():
    return {"message":"Welcome to FastAPI"}

@app.get("/about")
def about():
    return {
        "message":"welcome to about page",
        "details":{
            "name":"sit college",
            "location":"mangalore",
            "about":"sit college is one of the best engineering college in mangalore"
        }
            }

@app.get("/students")
def students_list():
    return {
        "message":"data loaded successfully",
        "data":students
    }

@app.post("/students")
def add_student(student: Student):
    students.append(student.model_dump())
    return {
        "message":"data posted successfully",
        "data":student
    }

@app.put("/students")
def update():
    students[0]["name"]="pramod"
    students[0]["age"]=25
    return {
        "message":"data updated successfully",
        "data":students
    }
@app.patch("/students")
def update():
    students[1]["name"]="pratham"
    return {
        "message":"data updated successfully",
        "data":students
    }
@app.delete("/students")
def delete():
    students.pop(0)
    return {
        "message":"data deleted successfully",
        "data":students
    }