from fastapi import HTTPException, status;
from sqlalchemy.orm import Session;

from app.schemas import JobCreate;
from app.models import Job;
from app.enums import JobStatus;

def create_job(job_data: JobCreate, db: Session) -> Job:
    job = Job(name=job_data.name, file=job_data.file);

    db.add(job);
    db.commit();
    db.refresh(job);

    return job;

def get_jobs(db: Session) -> list[Job]:
    return db.query(Job).all();

def get_job(job_id: int, db: Session) -> job | None:
    job = db.query(Job).filter(job_id == Job.id).first();
    return job;

def update_job_status(db: Session, job: Job, new_status: JobStatus) -> job:
    job.status = new_status.value;
    db.commit();
    db.refresh(job);
    return job;
