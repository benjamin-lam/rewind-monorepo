import chromadb
from chromadb.utils import embedding_functions
import os

class RewindEngine:
    def __init__(self, db_path="./data/chroma_db"):
        # Sicherstellen, dass der Pfad existiert
        if not os.path.exists(db_path):
            os.makedirs(db_path, exist_ok=True)
            
        self.client = chromadb.PersistentClient(path=db_path)
        
        # Lokales Embedding-Modell (Deutsch/Englisch)
        self.emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"
        )
        
        self.collection = self.client.get_or_create_collection(
            name="rewind_archive", 
            embedding_function=self.emb_fn
        )

    def save_thought(self, text, metadata):
        if not text.strip(): return
        doc_id = str(hash(text + str(metadata.get('bundle', ''))))
        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id]
        )

    def query_context(self, current_text, n_results=3):
        if len(current_text.strip()) < 15: return None
        return self.collection.query(
            query_texts=[current_text],
            n_results=n_results
        )
