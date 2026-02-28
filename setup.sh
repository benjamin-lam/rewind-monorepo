#!/bin/bash
# REWIND - Project Initializer Example

mkdir -p apps/core apps/web_ui data/chroma_db content/_templates scripts docs/worklogs

# Meta-Files schreiben (Inhalte von oben einfügen)
# ... (Ich kürze das hier ab, du kopierst die Blöcke einfach rein)

# Initialer Worklog-Eintrag
echo "# WORKLOG" > WORKLOG.md
echo "## [$(date +%Y-%m-%d)] - Die Geburt von REWIND" >> WORKLOG.md
echo "- Entscheidung für Mono-Repo und Bundle-Struktur getroffen." >> WORKLOG.md
echo "- Architektur-Vision definiert: 'Semantic Voice Recorder for Text'." >> WORKLOG.md

# Git Setup
git init
git checkout -b main
git add .
git commit -m "feat: REWIND initial engine setup"

echo "📼 REWIND ist bereit für den ersten Commit."
