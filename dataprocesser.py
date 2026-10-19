from pdf_reader import read_pdf
from chunk_creater import chunks_pages
from embedder import embedding_chunks
from vectorstore import pinecone_upsert
from typing import List


pdf_path="D:\clg project\RAG\pdf\Rajkumar1 Ai.pdf"

def run():
    pdf_content=read_pdf(pdf_path)
    chunks=chunks_pages(pdf_content)
    embeddings=embedding_chunks(chunks)
    print(f"Total chunks:{len(chunks)}")
    print(f"Total embeddings:{len(embeddings)}")
    pinecone_upsert(chunks,embeddings)

if __name__=="__main__":
    run()