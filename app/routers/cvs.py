from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.utils.pdf import extract_text_from_pdf


router = APIRouter(
    prefix="/cvs",
    tags=["CVs"],
)


@router.post("/upload")
async def upload_cv(
    file: UploadFile = File(...),
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are supported",
        )

    file_bytes = await file.read()

    text = extract_text_from_pdf(file_bytes)

    if not text:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Could not extract text from PDF",
        )

    return {
        "filename": file.filename,
        "characters": len(text),
        "text": text,
    }