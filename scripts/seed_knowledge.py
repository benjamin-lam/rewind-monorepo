import sys
import os

# Pfad-Hacking für Core-Import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from apps.core.engine import RewindEngine

def seed():
    engine = RewindEngine()
    
    knowledge_base = [
        {
            "text": "Technische Schulden in der KI-Ära: Durch Prompt Driven Development (PDD) entsteht Code schneller als je zuvor. Die Gefahr ist 'Instant Legacy Code' – Code, den niemand geschrieben hat, den niemand versteht, der aber produktiv ist.",
            "meta": {"bundle": "pdd-philosophy", "topic": "tech-debt"}
        },
        {
            "text": "Vibe-Coding beschreibt einen Zustand, in dem die Intention (der Vibe) wichtiger ist als die Syntax. Die Herausforderung: Wie dokumentiert man den 'Vibe', damit spätere Sprints nicht an fehlender technischer Spezifikation scheitern?",
            "meta": {"bundle": "vibe-coding-guide", "topic": "documentation"}
        },
        {
            "text": "In der KI-Arbeit verschieben sich technische Schulden von der 'Syntax-Ebene' auf die 'Kontext-Ebene'. Ein falscher Prompt führt nicht zu einem Syntax-Error, sondern zu einer falschen logischen Architektur, die erst Monate später auffällt.",
            "meta": {"bundle": "ai-development", "topic": "architecture"}
        },
        {
            "text": "Gegenmittel für KI-Schulden: 100% Transparenz im Worklog. Jede KI-Entscheidung muss für Menschen (und andere KIs) lesbar dokumentiert sein. REWIND nutzt genau diesen Ansatz durch das Mono-Repo-Prinzip.",
            "meta": {"bundle": "rewind-docs", "topic": "solution"}
        }
    ]

    print("🚀 Befülle REWIND mit PDD & Vibe-Coding Wissen...")
    for item in knowledge_base:
        engine.save_thought(item["text"], item["meta"])
        print(f"✅ Indiziert: {item['meta']['topic']}")

    print("\nKaboom! Dein REWIND-Gedächtnis ist nun scharf geschaltet.")

if __name__ == "__main__":
    seed()
