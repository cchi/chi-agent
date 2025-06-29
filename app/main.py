from fastapi import FastAPI
from llama_index import StorageContext, load_index_from_storage

from .openai_helper import get_openai_response

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to chi-agent"}


@app.get("/chat")
def chat(q: str):
    resp = get_openai_response(q)
    return {"response": resp}


@app.get("/search")
def search(q: str):
    storage_context = StorageContext.from_defaults(persist_dir="index")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    res = query_engine.query(q)
    return {"answer": str(res)}
