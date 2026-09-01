import pymupdf


def extract_text_from_pdf(file_bytes: bytes) -> str:
    document =pymupdf.open(
        stream=file_bytes,
        filetype="pdf",
    )

    text_parts = []

    for page in document:
        text_parts.append(page.get_text())

    document.close()

    return "\n".join(text_parts).strip()