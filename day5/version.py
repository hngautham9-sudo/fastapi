from fastapi import FastAPI

app=FastAPI()

@app.get("/profile/v1/{username}")
def profile(username:str):
        return{
                "message": f"welcome {username}"
        }

@app.get("/profile/v2/{username}")
def profile(username:str):
        return{
                "message": f"welcome {username}"
        }

