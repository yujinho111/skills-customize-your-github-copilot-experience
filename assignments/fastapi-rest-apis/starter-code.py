from fastapi import FastAPI

app = FastAPI(title="Book API")

# In-memory data store
books = [
    {"id": 1, "title": "Python Basics", "author": "A. Student", "year": 2024},
    {"id": 2, "title": "Data Structures", "author": "B. Builder", "year": 2023},
]

@app.get("/")
def home():
    return {"message": "Welcome to the Book API"}

# TODO: Add GET /books endpoint
# TODO: Add GET /books/{book_id} endpoint
# TODO: Add POST /books endpoint
# TODO: Add PUT or DELETE endpoints
