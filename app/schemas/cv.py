from pydantic import BaseModel


class Experience(BaseModel):
    role: str
    company: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    description: list[str] = []


class Project(BaseModel):
    name: str
    description: str | None = None
    technologies: list[str] = []


class Education(BaseModel):
    institution: str
    degree: str | None = None
    field: str | None = None
    start_date: str | None = None
    end_date: str | None = None


class Language(BaseModel):
    language: str
    level: str | None = None


class ParsedCV(BaseModel):
    name: str | None = None
    email: str | None = None

    skills: list[str] = []
    experiences: list[Experience] = []
    projects: list[Project] = []
    education: list[Education] = []
    languages: list[Language] = []