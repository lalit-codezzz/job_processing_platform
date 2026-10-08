from fastapi import APIRouter, HTTPException, status, Depends;
from sqlalchemy.orm import Session;

from app.schemas import JobResponse, JobCreate;
from app.database import get_db;
from app.models import Job;
from app.enums import JobStatus;
from app import crud;

router = APIRouter();

@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(status: str | None = None, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db);
    return jobs;


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):

    job = crud.get_job(job_id, db);

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found!");

    return job;


@router.post("/jobs", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    job = crud.create_job(job, db);
    return job;

@router.patch("/jobs/{job_id}/status", response_model=JobResponse)
def update_job_status(job_id: int, new_status: JobStatus, db: Session = Depends(get_db)):

    job = crud.get_job(job_id, db);

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found!");
    
    job = crud.update_job_status(db, job, new_status);

    return job;
