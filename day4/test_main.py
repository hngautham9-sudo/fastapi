from fastapi.testclient import TestClient
 
from project import app
 
client = TestClient(app)
 
 
def test_get_students():
 
	response = client.get("/students")
 
	assert response.status_code == 200
 
 
def test_add_student():
 
	response = client.post(
    	"/students",
    	json={
        	"RollNo": 2,
        	"name": "John",
        	"Age": 22
    	}
	)
 
	assert response.status_code == 200
 
	assert response.json()["message"] == \
    	"Student Added Successfully"
 
 
def test_update_student():
 
	response = client.put(
    	"/students/2",
    	json={
        	"RollNo": 2,
        	"name": "Magheswaran",
        	"Age": 23
    	}
	)
 
	assert response.status_code == 200
 
	assert response.json()["message"] == \
    	"Student Updated Successfully"
 
 
def test_update_student_age():
 
	response = client.patch(
    	"/students/2?age=25"
	)
 
	assert response.status_code == 200
 
	assert response.json()["message"] == \
    	"Student Age Updated"
 
 
def test_delete_student():
 
	response = client.delete(
    	"/students/2"
	)
 
	assert response.status_code == 200
 
	assert response.json()["message"] == \
    	"Student Deleted Successfully"



