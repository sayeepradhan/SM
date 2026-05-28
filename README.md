# Student Management API

A simple RESTful API built using FastAPI and SQLAlchemy for managing student records. The API supports CRUD operations to create, read, update, and delete student data including student ID, name, and marks.

---

## Features

- Get all students
- Get student by ID
- Add new student
- Update student details
- Delete student
- FastAPI backend
- SQLAlchemy ORM integration
- Structured project architecture

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

---

## Project Structure

```bash
student-management-api/
│
├── main.py
├── database.py
│
├── routes/
│   └── student_routes.py
│
├── models/
│   └── student_model.py
│
├── schemas/
│   └── student_schema.py
│
├── requirements.txt
└── README.md
```

---

## API Endpoints

### GET All Students

```http
GET /students
```

### GET Student By ID

```http
GET /students/{id}
```

### POST Create Student

```http
POST /students
```

#### Request Body

```json
{
  "id": 1,
  "name": "Rahul",
  "marks": 85
}
```

---

### PUT Update Student

```http
PUT /students/{id}
```

#### Request Body

```json
{
  "name": "Rahul Sharma",
  "marks": 90
}
```

---

### DELETE Student

```http
DELETE /students/{id}
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd student-management-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## API Documentation

FastAPI automatically generates API docs:

### Swagger UI

```bash
http://localhost:8000/docs
```

### ReDoc

```bash
http://localhost:8000/redoc
```

---

## Example Student Model

```python
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    marks = Column(Integer, nullable=False)
```

---

## Future Improvements

- Authentication & Authorization
- Pagination
- Search functionality
- Docker support
- Unit testing

---
Made by Sayee Pradhan

GitHub: https://github.com/sayeepradhan

---

