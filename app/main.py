from fastapi import FastAPI

from app.database import Base, engine
from app.routers.cvs import router as cvs_router
from app.routers.jobs import router as jobs_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CV Scoring API",
    version="0.1.0",
)


app.include_router(jobs_router)
app.include_router(cvs_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}