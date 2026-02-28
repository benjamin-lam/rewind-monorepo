from sentence_transformers import SentenceTransformer
import os

model_name = "paraphrase-multilingual-MiniLM-L12-v2"
print(f"🔄 Prüfe/Lade Modell: {model_name}...")
print("Dies kann je nach Leitung und CPU 5-10 Minuten dauern.")

model = SentenceTransformer(model_name)

print("✅ Modell erfolgreich geladen und im Cache gespeichert!")
# Das Modell liegt unter ~/.cache/torch/sentence_transformers/ (Linux/Mac)
# oder C:\Users\NAME\.cache\torch\sentence_transformers\ (Windows)
