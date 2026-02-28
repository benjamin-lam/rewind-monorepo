import os
import sys
from pathlib import Path

# Pfad-Hacking für Core-Import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from apps.core.engine import RewindEngine

def import_markdown_folder(target_folder):
    engine = RewindEngine()
    folder_path = Path(target_folder)
    
    if not folder_path.exists():
        print(f"❌ Ordner {target_folder} nicht gefunden!")
        return

    print(f"📂 Starte Import aus: {target_folder}")
    count = 0
    
    for md_file in folder_path.glob("**/*.md"):
        bundle_name = md_file.parent.name
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            # Wir speichern das ganze File als einen Gedanken-Block für den Start
            engine.save_thought(content, {
                "bundle": bundle_name, 
                "file": md_file.name,
                "type": "imported_archive"
            })
            count += 1
            print(f"  + {md_file.name} (Bundle: {bundle_name})")

    print(f"✅ Fertig! {count} Dateien in REWIND integriert.")

if __name__ == "__main__":
    # Standardmäßig importieren wir aus dem source_imports Ordner
    import_markdown_folder("./source_imports")
