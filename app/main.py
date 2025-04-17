from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import tempfile
from pathlib import Path
from .pdf_utils import pdf_to_text, create_text_pdf

app = FastAPI()

@app.post("/extract_text_pdf")
async def extract_text_pdf(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_input:
        temp_input.write(await file.read())
        temp_input_path = Path(temp_input.name)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_output:
        temp_output_path = Path(temp_output.name)

    text = pdf_to_text(temp_input_path)
    create_text_pdf(text, temp_output_path)

    return FileResponse(path=temp_output_path, filename="extracted_text.pdf", media_type='application/pdf')
