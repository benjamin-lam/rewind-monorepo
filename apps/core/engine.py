import chromadb
from chromadb.utils import embedding_functions

class RewindEngine:
    def __init__(self, db_path="./data/chroma_db"):
        self.client = chromadb.PersistentClient(path=db_path)
        # Lokales Modell, das keine Internetverbindung braucht
        self.emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"
        )
        self.collection = self.client.get_or_create_collection(
            name="rewind_archive", 
            embedding_function=self.emb_fn
        )

    def save_thought(self, text, metadata):
        """Speichert einen Text-Schnipsel oder Absatz."""
        self.collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[str(hash(text + metadata.get('bundle', '')))]
        )

    def query_context(self, current_text, n_results=3):
        """Findet semantisch ähnliche Gedanken aus der Vergangenheit."""
        if len(current_text.strip()) < 10: return None
        return self.collection.query(
            query_texts=[current_text],
            n_results=n_results
        )
