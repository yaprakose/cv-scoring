from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.job import JobCreate, JobResponse
from app.services.job_service import (
    create_job,
    get_job_by_id,
    get_jobs,
)


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.post(
    "",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_job_endpoint(
    job_data: JobCreate,
    db: Session = Depends(get_db),
):
    return create_job(
        db=db,
        job_data=job_data,
    )


@router.get(
    "",
    response_model=list[JobResponse],
)
def get_jobs_endpoint(
    db: Session = Depends(get_db),
):
    return get_jobs(db)


@router.get(
    "/{job_id}",
    response_model=JobResponse,
)
def get_job_endpoint(
    job_id: int,
    db: Session = Depends(get_db),
):
    job = get_job_by_id(
        db=db,
        job_id=job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )

    return job