from fastapi import FastAPI
from pydantic import BaseModel, Field
 
# Create FastAPI Application
app = FastAPI()
 
# Student Model with Validation Rules
class Student(BaseModel):
 
	# Name must contain 3 to 20 characters
	name: str = Field(
    	min_length=3,
    	max_length=20
	)
 
	# Age must be greater than 18 and less than 30
	age: int = Field(
    	gt=18,
    	lt=30
	)
 
# Create Student Endpoint
@app.post("/student")
def create_student(student: Student):
 
	return {
    	"message": "Student Created",
    	"student": student
	}



