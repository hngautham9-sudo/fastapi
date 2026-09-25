from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

students=[{"RollNo":1,"name":"Praveen","Age":21}]

class Student(BaseModel):
    RollNo:int
    name:str
    Age:int

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def add_student(student:Student):
    new_student=student.model_dump()
    students.append(new_student)
    return {"message":"Student Added Successfully","data":new_student}

@app.put("/students/{rollNo}")
def update_student(rollNo:int,student:Student):
    for student_record in students:
        if student_record["RollNo"]==rollNo:
            student_record["RollNo"]=student.RollNo
            student_record["name"]=student.name
            student_record["Age"]=student.Age
            return {"message":"Student Updated Successfully","data":student_record}
    return {"message":"Student Not Found"}

@app.patch("/students/{rollNo}")
def update_student_age(rollNo:int,age:int):
    for student_record in students:
        if student_record["RollNo"]==rollNo:
            student_record["Age"]=age
            return {"message":"Student Age Updated","data":student_record}
    return {"message":"Student Not Found"}

@app.delete("/students/{rollNo}")
def delete_student(rollNo:int):
    for student_record in students:
        if student_record["RollNo"]==rollNo:
            students.remove(student_record)
            return {"message":"Student Deleted Successfully","data":student_record}
    return {"message":"Student Not Found"}


