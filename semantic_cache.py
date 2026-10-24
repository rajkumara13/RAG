import sqlite3
import json
import numpy as np
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "semantic_cache.db"
SIMILARITY_THRESHOLD = 0.90

def initialize_cache():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS semantic_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                embedding TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        """)
def find_cached_answer(query_embedding):
    query_vector = np.asarray(query_embedding, dtype=float)
    query_norm = np.linalg.norm(query_vector)

    if query_norm == 0:
        return None

    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT embedding, answer FROM semantic_cache"
        ).fetchall()

    best_answer = None
    best_score = -1.0

    for embedding_json, answer in rows:
        cached_vector = np.asarray(
            json.loads(embedding_json), dtype=float
        )
        cached_norm = np.linalg.norm(cached_vector)

        if cached_norm == 0:
            continue

        score = float(
            np.dot(query_vector, cached_vector)
            / (query_norm * cached_norm)
        )

        if score > best_score:
            best_score = score
            best_answer = answer

    if best_score >= SIMILARITY_THRESHOLD:
        print(f"Semantic cache HIT: {best_score:.3f}")
        return best_answer

    print("Semantic cache MISS")
    return None


def save_cached_answer(query, query_embedding, answer):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO semantic_cache (query, embedding, answer)
            VALUES (?, ?, ?)
        """, (
            query,
            json.dumps(query_embedding),
            answer
        ))


initialize_cache()
