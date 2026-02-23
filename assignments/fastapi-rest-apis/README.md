# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small RESTful API using the FastAPI framework to practice routing, request/response handling, and basic CRUD operations.

## 📝 Tasks

### 🛠️	Create a REST API service

#### Description
Create a FastAPI application that exposes a small set of endpoints to manage an in-memory collection of items. Implement endpoints to list items, retrieve an item by id, create new items, update existing items, and delete items. Use JSON for request and response bodies and include basic validation.

#### Requirements
Completed program should:

- Provide a `GET /items` endpoint that returns all items.
- Provide `GET /items/{id}` to retrieve a single item by id (404 when not found).
- Provide `POST /items` to create a new item (return 201 and the created object).
- Provide `PUT /items/{id}` or `PATCH /items/{id}` to update an item.
- Provide `DELETE /items/{id}` to remove an item.
- Use Pydantic models for request/response schemas and return appropriate HTTP status codes.
- Include example requests and basic run instructions.

#### Example
Run the app locally with `uvicorn starter_code.main:app --reload --port 8000` and try commands like:

```
curl http://localhost:8000/items
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"name":"Notebook","price":4.99}'
```

## 🧩 Starter Files

- `starter_code/main.py`: Minimal FastAPI app with in-memory storage and CRUD endpoints.
- `requirements.txt`: Dependencies for running the app (`fastapi`, `uvicorn`).
