from fastapi import FastAPI, HTTPException


app = FastAPI()


# Secret API Key
API_KEY = "abc123"


# Public Endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


# Protected Endpoint
@app.get("/secure_data")
def secure_data(api_key: str):


    # Check whether API Key is valid
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )


    # Access granted
    return {
        "message": "Access Granted"
    }



