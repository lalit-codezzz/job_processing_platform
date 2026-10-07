from fastapi import FastAPI, status, HTTPException;

from schemas import JobCreate, JobResponse;

app = FastAPI();

@app.get("/")
def root():
    return {"message": "Job processing platform API"};

@app.get("/jobs")
def get_jobs(status: str | None = None):
    return {
        "status": status,
        "jobs": [],
    }

@app.get("/jobs/{job_id}")
def get_job(job_id: int):

    if (job_id != 1):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found!");

    return {
        "job_id": job_id,
        "status": "queued",
    }

@app.post("/jobs", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate):
    return {
        "id": 1,
        "name": job.name,
        "status": "queued",
    };