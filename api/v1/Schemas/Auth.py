
from pydantic import BaseModel , EmailStr


class Register(BaseModel):
    email: EmailStr
    phone_number: str
    name: str
    profession: list[str]
    institution: str

    password: str

class Login(BaseModel):
    email: EmailStr
    password: str
