# 🔧 Technische Spezifikationen

### Der Motor: ChromaDB
- **Modus:** PersistentClient (Lokale SQLite-Basis).
- **Embedding:** `paraphrase-multilingual-MiniLM-L12-v2` (Lokal, CPU-optimiert).

### Der Antrieb: Python & Mono-Repo
- **Struktur:** Content-Bundles (Markdown + Assets + Metadata).
- **Git-Integration:** Hooks für automatische Re-Indizierung bei Commits.

### Wartung:
- **Ölwechsel:** `pip install --upgrade` der Core-Libs.
- **Wischwasser:** `chroma_manager.py` zur Bereinigung verwaister Vektoren.
