from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    marks: int


class StudentOut(BaseModel):
    id: int
    name: str
    marks: int

    class Config:
        orm_mode = True
       