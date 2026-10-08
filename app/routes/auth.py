from fastapi import APIRouter, HTTPException, Depends, status;
from sqlalchemy.orm import Session;

from app import crud;
from app.models import User;
from app.database import get_db;
from app.schemas import UserResponse, UserCreate;

router = APIRouter(prefix="/auth", tags=["Authentication"]);

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == user_data.email).first();

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with email already exists!");

    return crud.create_user(user_data, db);

# @router.get("/users")
# def get_users(db: Session = Depends(get_db)):
#     return crud.get_users(db);