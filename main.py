from fastapi import FastAPI
from db import engine, Base
from routes import student

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student.router)

