from fastapi import HTTPException, status;
from sqlalchemy.orm import Session;

from app.schemas import JobCreate, UserCreate;
from app.enums import JobStatus;
from app.models import Job, User;

# Job related: --------------------------------------------------------------------------------

def create_job(job_data: JobCreate, db: Session) -> Job:
    job = Job(name=job_data.name, file=job_data.file);

    db.add(job);
    db.commit();
    db.refresh(job);

    return job;

def get_jobs(db: Session) -> list[Job]:
    return db.query(Job).all();

def get_job(job_id: int, db: Session) -> Job | None:
    job = db.query(Job).filter(job_id == Job.id).first();
    return job;

def update_job_status(db: Session, job: Job, new_status: JobStatus) -> Job:
    job.status = new_status.value;
    db.commit();
    db.refresh(job);
    return job;


# User related: ------------------------------------------------------------------------------

def create_user(user_data: UserCreate, db: Session) -> User:
    user = User(email=user_data.email, hashed_password=user_data.password);

    db.add(user);
    db.commit();
    db.refresh(user);
    return user;

# def get_users(db: Session) -> User:
#     return db.query(User).all();