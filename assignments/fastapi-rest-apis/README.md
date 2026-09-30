# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using Python and FastAPI to manage a collection of books or items. Students will practice creating routes, handling JSON data, and responding to client requests.

## 📝 Tasks

### 🛠️ Create the API Foundation

#### Description
Set up a FastAPI application that exposes a simple API for managing a list of resources.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define at least one `GET` endpoint that returns data in JSON format
- Return a list of sample items or records when the endpoint is called
- Run the app locally with Uvicorn or FastAPI's built-in development server

### 🛠️ Add CRUD Functionality

#### Description
Extend the API so it can create, read, update, and delete records.

#### Requirements
Completed program should:

- Add a `GET /items` endpoint to display all items
- Add a `GET /items/{item_id}` endpoint to fetch one item by ID
- Add a `POST /items` endpoint to create a new item
- Add a `PUT` or `PATCH` endpoint to update an existing item
- Add a `DELETE /items/{item_id}` endpoint to remove an item
- Use Python dictionaries or a simple in-memory list to store data

### 🛠️ Validate and Document the API

#### Description
Improve the API by adding validation and clear response models for a more professional design.

#### Requirements
Completed program should:

- Use Pydantic models to validate incoming request data
- Return clear JSON responses for success and error cases
- Include helpful route descriptions and response examples in the API documentation
- Test the endpoints using FastAPI's built-in docs at `/docs` or `/redoc`
