from openai import OpenAI
from dotenv import load_dotenv
from typing import List
from sentence_transformers import SentenceTransformer

model=SentenceTransformer('all-MiniLM-L6-v2')

load_dotenv()

"""client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
Embedding_MODEL="text-embedding-3-small"

def embedding_chunks(chunks:List[str])->List[List[float]]:
    embeddings=[]
    for chunk in chunks:
        response=client.embeddings.create(
            input=chunk,
            model=Embedding_MODEL
        )
        embeddings.append(response.data[0].embeddings)
    return embeddings
"""

def embedding_chunks(chunks:List[str])->List[List[float]]:
    embeddings=model.encode(
        chunks,
        convert_to_numpy=True
        )
    return embeddings.tolist()

def embedding_query(query:str)->List[float]:
    embedding=model.encode(
        query,
        convert_to_numpy=True
        )
    return embedding.tolist()

    
from chunk_creater import chunks_pages
from pdf_reader import read_pdf

""" pdf_path="D:\clg project\RAG\pdf\Rajkumar1 Ai.pdf"
pdf_content=read_pdf(pdf_path)
chunks=chunks_pages(pdf_content)
embeddings=embedding_chunks(chunks)
print(f"Total chunks: {len(chunks)}")
print(f"Total embeddings: {len(embeddings)}")   
print(f"Sample chunk: {chunks[0]}")
print(f"Sample embedding: {embeddings[0]}")
"""