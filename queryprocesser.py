from llm import generate_response
from embedder import embedding_query
from vectorstore import pinecone_query

def process_query(query:str)->str:
    query_embedding=embedding_query(query)
    matched_chunks=pinecone_query(query_embedding,top_k=4)
    generated_response=generate_response(query,matched_chunks)

    print(generated_response)


if __name__=="__main__":
    user_query=input("Enter your query: ")
    process_query(user_query)