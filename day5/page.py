from fastapi import FastAPI
 
app = FastAPI()
 
students = [
 
	{"RollNo": 1, "name": "Praveen"},
	{"RollNo": 2, "name": "Rahul"},
	{"RollNo": 3, "name": "Arun"},
	{"RollNo": 4, "name": "Ravi"},
	{"RollNo": 5, "name": "Kiran"},
	{"RollNo": 6, "name": "Naveen"},
	{"RollNo": 7, "name": "Ajay"},
	{"RollNo": 8, "name": "Vijay"},
	{"RollNo": 9, "name": "Deepak"},
	{"RollNo": 10, "name": "John"},
	{"RollNo": 11, "name": "Suresh"},
	{"RollNo": 12, "name": "Mahesh"},
	{"RollNo": 13, "name": "Rakesh"},
	{"RollNo": 14, "name": "Ganesh"},
	{"RollNo": 15, "name": "Dinesh"}
 
]
 
@app.get("/students")
def get_students(skip: int, limit: int):
 
	return students[skip:skip + limit]

