from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "My first API is working!"}


@app.get("/books")
def get_books():
    books = [
        {
            "title": "Dune",
            "author": "Frank Herbert",
            "year": 1965
        },
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "year": 1937
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "year": 1949
        }
    ]

    return books


@app.get("/student")
def get_student():
    return {
        "name": "David",
        "age": 20,
        "is_student": False,
        "subjects": ["Python", "Math", "English"]
    }


@app.get('/appointments/{appointment_id}')
def get_appointment(appointment_id: int):
    return {
        'appointment_id': appointment_id,
        'status': 'confirmed'
    }
