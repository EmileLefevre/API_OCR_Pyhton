from pdf2image import convert_from_path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pathlib import Path
from .ocr_utils import extract_text_from_image


def pdf_to_text(pdf_path: Path) -> str:
    """
    Convertit un PDF en texte en utilisant OCR sur chaque image du PDF.
    """
    images = convert_from_path(str(pdf_path))
    all_text = []
    for image in images:
        text = extract_text_from_image(image)
        all_text.append(text)
    return "\n\n".join(all_text)


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_text_pdf(text, output_path):
    c = canvas.Canvas(str(output_path), pagesize=letter) 
    c.setFont("Helvetica", 10)

    width, height = letter
    margin = 40
    max_line_length = width - 2 * margin
    y_position = height - margin

    lines = text.splitlines()

    for line in lines:
        if y_position < margin:
            c.showPage()
            c.setFont("Helvetica", 10)
            y_position = height - margin

        words = line.split()
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            if c.stringWidth(test_line) < max_line_length:
                current_line = test_line
            else:
                c.drawString(margin, y_position, current_line)
                y_position -= 12
                current_line = word

        if current_line:
            c.drawString(margin, y_position, current_line)
            y_position -= 12

    c.save()



def process_pdf_and_create_output(pdf_path: Path, output_pdf_path: Path):
    """
    Extrait le texte du PDF et crée un PDF contenant ce texte.
    """
    try:
        extracted_text = pdf_to_text(pdf_path)
        print(f"Texte extrait : {extracted_text[:200]}...")

        create_text_pdf(extracted_text, output_pdf_path)
        print(f"Le PDF a été créé avec succès à {output_pdf_path}")
    except Exception as e:
        print(f"Erreur lors du traitement du PDF : {e}")


pdf_path = Path("/chemin/vers/votre/document.pdf")
output_pdf_path = Path("/chemin/vers/le/pdf_de_sortie.pdf")
process_pdf_and_create_output(pdf_path, output_pdf_path)
