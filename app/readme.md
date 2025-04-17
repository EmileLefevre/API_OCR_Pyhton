# PDF OCR API

Une API FastAPI pour extraire le texte de fichiers PDF scannés (avec OCR) et générer un nouveau PDF avec le texte reconnu.

---

## 📦 Installation

```bash
git clone <url_du_repo>
cd <nom_du_dossier>


2. Créer un environnement virtuel :
    python3 -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate

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
