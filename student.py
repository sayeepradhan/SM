from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas
from db import SessionLocal

router = APIRouter()

# ---------------------------
# DB SESSION
# ---------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------
# CREATE STUDENT (POST)
# ---------------------------
@router.post("/students")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):

    new_student = models.Student(
        name=student.name,
        marks=student.marks
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# ---------------------------
# READ ALL STUDENTS (GET)
# ---------------------------
@router.get("/students")
def get_students(db: Session = Depends(get_db)):

    return db.query(models.Student).all()


# ---------------------------
# READ SINGLE STUDENT (GET by ID)
# ---------------------------
@router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# ---------------------------
# UPDATE STUDENT (PUT)
# ---------------------------
@router.put("/students/{student_id}")
def update_student(student_id: int, updated: schemas.StudentCreate, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name = updated.name
    student.marks = updated.marks

    db.commit()
    db.refresh(student)

    return student


# ---------------------------
# DELETE STUDENT (DELETE)
# ---------------------------
@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):

    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}