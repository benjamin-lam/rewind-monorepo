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

## Der erste Start
Jetzt kannst du die App zünden:

streamlit run apps/web_ui/main.py

## Was jetzt passieren sollte:
Beim ersten Start lädt Python das Sentence-Transformer Modell (ca. 500MB) herunter. Das passiert nur einmal. Danach öffnet sich dein Browser unter localhost:8501.

    ### irgendwie passiert da nichts.
    führe das mit python3 check_model.py aus. Hier siehst du Fehlermeldungen oder Fortschritte direkt.
    Ressourcen-Monitor (Task-Manager / htop)

    Windows: Strg + Umschalt + Esc -> Tab "Leistung" -> Schau auf Netzwerk (lädt er Daten?) und Datenträger (schreibt er viel?).
    Mac/Linux: Tippe top oder htop im Terminal. Suche nach dem Prozess python3. Wenn er bei 100% CPU steht, rechnet er gerade das Modell klein.

   Warum das "Warten" bei REWIND anders ist:
   Im Gegensatz zu ChatGPT, wo die Cloud rechnet, findet hier gerade die "Einschulung" deines eigenen Rechners statt. Sobald das Modell einmal im Ordner .cache auf deiner Festplatte liegt, startet die App beim nächsten Mal in Sekunden, da nichts mehr      geladen werden muss.

   Pro-Tipp für langsame Rechner (Phase 1 Fix):
   Falls dein RAM (unter 8GB) der Flaschenhals ist, können wir in der engine.py später auf ein noch kleineres Modell umsteigen (z.B. paraphrase-multilingual-MiniLM-L3-v2), das nur ca. 150MB groß ist.
   Soll ich warten, bis dein check_model.py grünes Licht gibt, oder möchtest du direkt wissen, wie wir das Modell verkleinern, falls dein Rechner kapituliert?
   @todo Anleitung kleineres Modell einbinden.
   something like:
   Ändere die Zeile in deiner check_model.py:
   
   # Tausche L12 gegen L6 oder L3 (L6 ist ein guter Kompromiss)
   model_name = "paraphrase-multilingual-MiniLM-L6-v2"

## Status-Check:
- Ordner apps/core/ enthält engine.py?
- Ordner apps/web_ui/ enthält main.py?
- requirements.txt ist installiert?

## Der "Magic Moment" Test
Nachdem du das Skript ausgeführt hast (python3 scripts/seed_knowledge.py), starte deine App:
streamlit run apps/web_ui/main.py

### Teste folgendes im Editor:
Tippe den Satz: "Ich mache mir Sorgen über Code, den die KI generiert, aber keiner versteht."

### Was passieren sollte:
Auf der rechten Seite (Inspiration) sollte REWIND dir sofort den Block über "Instant Legacy Code" vorschlagen.

### Warum dieses Thema für REWIND so wichtig ist
Durch das Ingestieren dieser Thesen wird deine App zum Dogfooding-Tool:

    Du nutzt eine KI-gestützte App (REWIND), um über die Gefahren von KI-generierten Schulden zu schreiben.
    REWIND hilft dir dabei, deine eigene Dokumentations-Philosophie (Worklog, Transparenz) konsequent durchzuziehen.

## Status-Check für dein Mono-Repo:

    apps/core/engine.py (Das Gehirn läuft)
    apps/web_ui/main.py (Das Cockpit zeigt Daten an)
    scripts/seed_knowledge.py (Das Wissen ist in der DB)


