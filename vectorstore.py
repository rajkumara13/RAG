from pinecone import Pinecone
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()

pinecone_client=Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index=pinecone_client.index(os.getenv("PINCONE_INDEX_NAME"))

def pinecone_upsert(chunks:List[str],embeddings:List[List[float]]):
    if len(chunks)!=len(embeddings):
        raise ValueError("The number of chunks and embeddings must be the same.")
    vector_data=[]
    for i,(chunk,embedding) in enumerate(zip(chunks,embeddings)):
        vector_values={
        "id":f"chunk_{i}",
        "values":embedding, 
        "metadata":{"text":chunk,
                    "chunk_index":i}

        }
        vector_data.append(vector_values)
    batch_size=100
    for i in range(0,len(vector_data),batch_size):
        batch=vector_data[i:i+batch_size]
        index.upsert(vectors=batch)


def pinecone_query(query_embedding:List[float],top_k: int =4):
    results=index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )
    print(f"Found {len(results.matches)} matches for the query.")
    matched_chunks=[]
    for match in results.matches:
        matched_chunks.append(match.metadata.get("text"))
    return matched_chunks
