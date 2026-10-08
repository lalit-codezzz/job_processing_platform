from fastapi import FastAPI;

from app.routes.jobs import router as jobs_router;
from app.routes.auth import router as auth_router;

app = FastAPI();

app.include_router(jobs_router);
app.include_router(auth_router);

@app.get("/")
def root():
    return {"message": "Job processing platform API"};
