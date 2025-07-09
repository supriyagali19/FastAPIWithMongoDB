FastAPI Employee Management API
A simple and efficient REST API for managing employee data, built with FastAPI and MongoDB. This application provides complete CRUD (Create, Read, Update, Delete) functionality for an employee database.

Features
Asynchronous: Built on top of async and await for high-performance, non-blocking I/O.

Data Validation: Uses Pydantic for robust data validation, serialization, and documentation.

CRUD Operations: Full support for creating, reading, updating, and deleting employee records.

MongoDB Integration: Connects to a MongoDB database for persistent data storage.

Clean Architecture: Organized structure with separation of concerns for API routes, database models, and configuration.

Secure Configuration: Manages sensitive keys (like database URIs) securely using environment variables.

Tech Stack
Framework: FastAPI

Database: MongoDB (with Pymongo)

Data Validation: Pydantic

ASGI Server: Uvicorn

Configuration: python-dotenv

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing.

Prerequisites
Python 3.8+

Git

A MongoDB database instance (local or on MongoDB Atlas)

Installation
Clone the repository

git clone https://github.com/supriyagali19/FastAPIWithMongoDB.git
cd FastAPIWithMongoDB

Create and activate a virtual environment (Recommended)

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required dependencies

pip install -r requirements.txt

Set up your environment variables

Create a file named .env in the root of the project.

Add your MongoDB connection string to this file.

MONGODB_URI="your_mongodb_connection_string_goes_here"

Run the application

uvicorn working:app --reload

The API will now be running at http://127.0.0.1:8000.

API Documentation
Once the application is running, you can access the interactive API documentation at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

API Endpoints
All endpoints are available under the /api/v1/ prefix.

Method

Endpoint

Description

GET

/

Get all employees

GET

/{id}

Get a single employee by ID

POST

/

Create a new employee

PUT

/{id}

Update an employee by ID

DELETE

/{id}

Delete an employee by ID

Example: Create a New Employee
Request: POST /api/v1/

Body:

{
  "id": "EMP101",
  "name": "John Doe",
  "age": 32,
  "department": "Development",
  "salary": 85000.50
}

Successful Response (200 OK):

{
  "message": "Employee created successfully",
  "employee": {
    "id": "EMP101",
    "name": "John Doe",
    "age": 32,
    "department": "Development",
    "salary": 85000.50
  }
}

Project Structure
.
├── .gitignore
├── configurations.py   # Database connection and setup
├── database/
│   ├── models.py       # Pydantic models for data validation
│   └── schema.py       # Helper functions to format DB data
├── requirements.txt    # Project dependencies
├── working.py          # Main FastAPI application and API routes
└── README.md

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
