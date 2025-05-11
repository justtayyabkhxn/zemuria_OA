from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

router = APIRouter()


class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

@router.post("/openai/chat", response_model=QueryResponse)
async def query_openai(request: QueryRequest):
    try:
        llm = ChatOpenAI(
            temperature=0.7,
            model_name="gpt-3.5-turbo",
            openai_api_key="",
        )
        response = llm([HumanMessage(content=request.query)])
        return {"response": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
