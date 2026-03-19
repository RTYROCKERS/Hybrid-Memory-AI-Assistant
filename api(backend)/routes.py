from fastapi import FastAPI
from models import ChatRequest
import sys
sys.path.insert(0,"../pipeline(rag)")
from pipeline import Rag_pipeline
sys.path.insert(0,"../llm")
from llm_config import client
sys.path.insert(0,"../vector_db_context")
from dbase_config import collection

app=FastAPI()

@app.post("/chat")
def memory_based_response(request:ChatRequest):
    pipeline=Rag_pipeline(llm=client,collection=collection)
    answer=pipeline.run(request.query)
    return {'response': answer} 