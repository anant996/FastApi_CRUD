# CRUD API with FastAPI

This project is a CRUD (Create, Read, Update, Delete) API built using FastAPI, a modern web framework for building APIs with Python. The API allows users to perform operations on a user database, including creating, retrieving, updating, and deleting user records.

## Introduction

The CRUD API is designed to provide a simple yet powerful interface for managing user records. It follows best practices for API design and utilizes FastAPI's capabilities for efficient and scalable development.

## Features

- Create new user records
- Retrieve user details by ID
- Update user information
- Delete user records
- Retrieve all user records

## Dependencies
 
1. Pydantic: Pydantic is a powerful data validation and settings management library for Python. It allows you to define data schemas and validate input data against those schemas. In this repository, Pydantic is utilized extensively for data validation.
   
      In this repo i am using pydantic's base model for data validation.
   
      Base Model:
      Pydantic provides a BaseModel class, which serves as the foundation for defining data models with validation rules.
      
      User Model Example:
      ```
      from pydantic import BaseModel, Field
      
      class User(BaseModel):
          id: int = Field(..., gt=0, description="User ID must be greater than zero")
          name: str = Field(..., min_length=1, max_length=100, description="User name must be between 1 and 100 characters")
      ```
      id: An integer representing the user ID. It is validated to be greater than zero.
   
      name: A string representing the user's name. It is validated to be between 1 and 100 characters in length.

2. APIRouter: APIRouter is a fastapi utility that helps in organizing API endpoints and handling requests in FastAPI applications. It allows you to define routes for different HTTP methods and group related endpoints together.
   
3. HTTPException: HTTPException is an exception class provided by FastAPI for handling HTTP errors. It allows you to raise HTTP errors with specific status codes and error messages, which are automatically translated into appropriate HTTP responses.

      Commonly Used HTTP Status Codes:
   
      **400 Bad Request**: The server cannot process the request due to a client error, such as syntax error or invalid parameters.
      
      **401 Unauthorized**: The request lacks valid authentication credentials or authorization for the requested resource.
      
      **404 Not Found**: The server cannot find the requested resource. It may be removed, renamed, or temporarily unavailable.
      
      **200 OK**: The request has succeeded, and the server has returned the requested content.
      
      **500 Internal Server Error**: A generic error message indicating that something has gone wrong on the server's end. It is often used for unexpected errors that are not handled by specific error codes.

## Project Structure

```
FastApi_CRUD/
├── app/
│ ├── endpoints/
│ │ ├── __init__.py
│ │ └── user_endpoints.py
│ ├── services/
│ │ ├── __init__.py
│ │ └── user_services.py
│ ├── utils/
│ │ ├── __init__.py
│ │ └── dummy_db.py
│ ├── __init__.py
│ └── main.py
│ └── models.py
├── .gitignore
└── requirements.txt
└── README.md
└── setup.py

```

## Installation

To run the CRUD API locally, follow these steps:

1. Clone the repository:
   
    ```git clone https://github.com/anant996/FastApi_CRUD.git```

2. Navigate to the project directory:
   
    ```cd FastApi_CRUD```

4. Set up a virtual environment:

    ```virtualenv venv```

5. Activate the virtual environment:

   On Windows:

   ```venv\Scripts\activate```

   On macOS/Linux:

   ```source venv/bin/activate```

6. Install the required dependencies:
   
    ```pip install -r requirements.txt```


## To start the API server, run the following command:

```
cd app

python3 -m uvicorn main:app --reload
```

## Testing

The project includes comprehensive unit tests to ensure the functionality and reliability of the CRUD API endpoints. These tests are written using pytest and the `TestClient` provided by FastAPI for testing API endpoints.


### Running Tests

To run the tests, navigate to the project directory and execute the following command:

```
cd FastApi_CRUD
pytest
```
