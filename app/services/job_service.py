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


def get_jobs(db: Session) -> list[Job]:
    return db.query(Job).order_by(Job.id.desc()).all()


def get_job_by_id(db: Session, job_id: int) -> Job | None:
    return db.query(Job).filter(Job.id == job_id).first()