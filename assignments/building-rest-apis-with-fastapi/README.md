# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a REST API using the FastAPI framework. You will practice defining endpoints, validating request data with Pydantic models, and returning structured JSON responses.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Build a FastAPI application for managing a simple collection of books.

#### Requirements
Completed program should:

- Create a FastAPI app in starter-code.py.
- Implement GET /books to return all books.
- Implement GET /books/{book_id} to return one book by ID or a clear not found response.


### 🛠️	Add Create and Update Operations

#### Description
Add endpoints that accept request bodies, validate input, and update stored data.

#### Requirements
Completed program should:

- Implement POST /books to add a new book with title, author, and published_year.
- Validate incoming data using a Pydantic model.
- Implement PUT /books/{book_id} to update an existing book and return the updated result.
