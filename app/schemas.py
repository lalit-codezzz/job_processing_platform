from pydantic import BaseModel;

class JobCreate(BaseModel):
    name: str;
    file: str;

class JobResponse(BaseModel):
    id: int;
    name: str;
    status: str;