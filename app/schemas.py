from pydantic import BaseModel, EmailStr;

class JobCreate(BaseModel):
    name: str;
    file: str;

class JobResponse(BaseModel):
    id: int;
    name: str;
    status: str;

class UserCreate(BaseModel):
    email: EmailStr;
    password: str;

class UserResponse(BaseModel):
    id: int;
    email: EmailStr;