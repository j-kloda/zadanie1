FROM python:3.10-slim

# Katalog roboczy
WORKDIR /app

# Kopia plików
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Uruchomienie aplikacji
CMD ["python", "app.py"]
