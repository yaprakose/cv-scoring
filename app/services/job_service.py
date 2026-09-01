from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import JobCreate


def create_job(db: Session, job_data: JobCreate) -> Job:
    job = Job(
        title=job_data.title,
        description=job_data.description,
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job