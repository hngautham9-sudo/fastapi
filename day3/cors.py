from fastapi import FastAPI


from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,


    allow_origins=["*"],


    allow_methods=["*"],


    allow_headers=["*"]
)


@app.get("/student")
def get_student():


    return {
        "name": "Ashok",
        "age": 20
    }

