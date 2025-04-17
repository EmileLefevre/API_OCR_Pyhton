# PDF OCR API

Une API FastAPI pour extraire le texte de fichiers PDF scannés (avec OCR) et générer un nouveau PDF avec le texte reconnu.

---

## 📦 Installation

```bash
git clone <https://github.com/EmileLefevre/API_OCR_Pyhton.git>
# ou en SSH : git clone <git@github.com:EmileLefevre/API_OCR_Pyhton.git>
cd <API Python>


2. Créer un environnement virtuel :
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    #pour sortir de venv -> deactivate

3. Installer les dépendances Python
    pip install -r requirements.txt

4. Installer les dépendances système
    macOS brew install poppler tesseract

    Ubuntu/Debian
        sudo apt update
        sudo apt install poppler-utils tesseract-ocr

5. Lancer l'API

uvicorn app.main:app --reload
L'API sera disponible à l'adresse :
http://127.0.0.1:8000/docs

```
