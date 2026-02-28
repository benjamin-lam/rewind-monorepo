import streamlit as st
import sys
import os

# Pfad-Hacking, damit wir den core-Ordner importieren können
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from apps.core.engine import RewindEngine

st.set_page_config(page_title="REWIND Editor", layout="wide")
engine = RewindEngine()

st.title("📼 REWIND Editor")

# Layout: Links Schreiben, Rechts Inspiration
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Dein Entwurf")
    bundle_name = st.text_input("Projekt-Name (Bundle):", value="unnamed-project")
    content = st.text_area("Schreib hier deine Gedanken...", height=500, key="editor")

    if st.button("💾 In REWIND speichern"):
        engine.save_thought(content, {"bundle": bundle_name, "type": "draft"})
        st.success("Gedanke archiviert!")

with col2:
    st.subheader("💡 Rewind: Das hast du mal gedacht...")
    if content:
        results = engine.query_context(content)
        if results and results['documents'][0]:
            for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
                with st.expander(f"Quelle: {meta.get('bundle', 'Unbekannt')}"):
                    st.write(doc)
        else:
            st.info("Noch keine ähnlichen Gedanken gefunden. Schreib weiter!")
