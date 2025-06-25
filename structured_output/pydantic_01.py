from pydantic import BaseModel , EmailStr # to validate the email installing pydantic[email]
from pydantic import Field
from typing import Optional

class Student(BaseModel):
    name: str 
    age: int = None #setting a default value as None making it optional here
    Gender: Optional[str] = None # another way of setting Optional value using typing Optional library
    email: EmailStr
    #Using Field as constraint
    cgpa: float = Field(gt=0,lt=10, description="the cgpa of the student") #imposes a contraint that it should be greater than 0 an dless than 10 and also adds description


new = {'name':'Susmita','email':'abc@gmail.com','cgpa':8}

student = Student(**new)
print(student)
print(dict(student))
print(student.model_dump_json)