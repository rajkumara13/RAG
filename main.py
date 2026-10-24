from fastapi import FastAPI,HTTPException
from queryprocesser import process_query
from pydantic import BaseModel

app=FastAPI(
    title="RAG API"
)

class QueryRequest(BaseModel):
    question:str

class QueryResponse(BaseModel):
    question:str
    answer:str
@app.get("/")
def home():
    return {"message": "The RAG api is running"}



@app.post("/ask",response_model=QueryResponse)
def ask_question(request:QueryRequest):
    question=request.question.strip()

    if not question:
        raise HTTPException(status_code=400,detail="question is not empty")

    try:
        answer=process_query(question)
        return QueryResponse(
            question=question,
            answer=answer
        )
    except Exception as e:
        raise HTTPException(status_code=500,detail="Failed the process" ) from e

    
