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

