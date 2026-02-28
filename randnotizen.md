# Randnotizen (blame76)

## Der "Kaboom"-Check (Installation)
Führe diese Befehle nacheinander aus, um die Umgebung "scharf" zu schalten:

### 1. Virtual Environment (falls noch nicht aktiv)
python3 -m venv venv
source venv/bin/activate

### 2. Dependencies installieren
pip install -r requirements.txt

### 3. Struktur-Check: Hast du den Datenordner?
mkdir -p data/chroma_db
