from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'laddi'
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5, description='A decimal value representaion')


new_student = {'name':'laddi', 'age':28, 'email':'xyz@gmail.com', 'cgpa':1}
# new_student = {'name':32}
# new_student = {}

student = Student(**new_student)
print(type(student))
print(student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()