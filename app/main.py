from fastapi import FastAPI


app = FastAPI(
    title="CV Scoring API",
    description="AI-powered CV and job description matching system",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "CV Scoring API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }