from llm import generate_response
from embedder import embedding_query
from vectorstore import pinecone_query
from semantic_cache import find_cached_answer, save_cached_answer



def process_query(query:str)->str:
    query=query.strip()

    if not query:
        raise ValueError("Query cannot be empty")
    
    # Generate embedding for the query
    query_embedding=embedding_query(query)

    # Check if the answer is already cached
    cached_answer=find_cached_answer(query_embedding)
    # If a cached answer is found, return it
    if cached_answer is not None:
        return cached_answer
    # If no cached answer is found, perform a vector search in Pinecone to find relevant chunks
    matched_chunks=pinecone_query(query_embedding,top_k=4)

    # Generate a response using the matched chunks and the original query
    generated_response=generate_response(query,matched_chunks)

    # Save the matched chunks in the semantic cache for future queries
    save_cached_answer(query,query_embedding,matched_chunks)


    

    return generated_response


if __name__=="__main__":
    user_query=input("Enter your query: ")
    print(process_query(user_query))
