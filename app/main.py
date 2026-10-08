from fastapi import FastAPI;

from app.routes.jobs import router as jobs_router;

app = FastAPI();

app.include_router(jobs_router);

@app.get("/")
def root():
    return {"message": "Job processing platform API"};
