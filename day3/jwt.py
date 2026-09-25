from fastapi import FastAPI, HTTPException
from jose import JWTError, jwt


SECRET_KEY = "mysecretkey_1234"
ALGORITHM = "HS256"


app = FastAPI()



def create_token(username: str):


    payload = {
        "username": username
    }


    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


    return token




def verify_token(token: str):


    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )


        return payload["username"]


    except JWTError:


        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )




@app.post("/login")
def login(uname: str, password: str):


    if uname == "admin" and password == "1234":


        token = create_token(uname)


        return {
            "access_token": token
        }


    raise HTTPException(
        status_code=400,
        detail="Invalid Username or Password"
    )




@app.get("/secure_data")
def secure_data(token: str):


    username = verify_token(token)


    return {
        "message": f"Hello {username}, Welcome to Secure API"
    }



