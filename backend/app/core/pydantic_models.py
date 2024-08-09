from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    id: int
    first_name: str
    second_name: str
    email: EmailStr
    phone_number: str


class RegistryUser(BaseModel):
    first_name: str
    second_name: str
    email: str
    phone_number: str
    password: str


class LoginUser(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str | None = None
