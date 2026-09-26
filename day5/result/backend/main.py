from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/results")
def get_results():


    return [
        {
            "student_name": "Rahul Kumar",
            "register_number": "22CS101",
            "department": "CSE",
            "subjects": [
                {
                    "subject_name": "Python Programming",
                    "grade": "A+"
                },
                {
                    "subject_name": "DBMS",
                    "grade": "A"
                },
                {
                    "subject_name": "REST API Development",
                    "grade": "B+"
                }
            ]
        },


        {
            "student_name": "Priya Sharma",
            "register_number": "22CS102",
            "department": "CSE",
            "subjects": [
                {
                    "subject_name": "Python Programming",
                    "grade": "A"
                },
                {
                    "subject_name": "DBMS",
                    "grade": "B+"
                },
                {
                    "subject_name": "REST API Development",
                    "grade": "A+"
                }
            ]
        },


        {
            "student_name": "Arun Kumar",
            "register_number": "22CS103",
            "department": "CSE",
            "subjects": [
                {
                    "subject_name": "Python Programming",
                    "grade": "B+"
                },
                {
                    "subject_name": "DBMS",
                    "grade": "A"
                },
                {
                    "subject_name": "REST API Development",
                    "grade": "A"
                }
            ]
        }
    ]



