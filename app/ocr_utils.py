from PIL import Image
import pytesseract

def extract_text_from_image(image: Image.Image) -> str:
    text = pytesseract.image_to_string(image, lang='fra') 
    return text.strip()
