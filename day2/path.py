from fastapi import FastAPI, HTTPException,status
app = FastAPI()


@app.get("/profile/{username}")
def profile(username:str,age:int):
    return {
        "message":f"Welcome to {username} profile page and your age is {age}",
    }

@app.get("/students",status_code=status.HTTP_201_CREATED)
def get_students():
	return {"message":"Student Created"}

@app.get("/students/{rollno}")
def student(rollno:int):
 
    if rollno != 1:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
 
    return {"Name":"Magesh"}
