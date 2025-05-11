from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

router=APIRouter()

class QueryRequest(BaseModel):
    query:str

class QueryResponse(BaseModel):
    response:str
    
@router.post("/api/query",response_model=QueryResponse)

async def query_openai(request:QueryRequest):
        try:
            llm=ChatOpenAI(
                temperature=0.7,
                model_name="gpt-3.5-turbo",
                openai_api_key="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",
            )
            response=llm([HumanMessage(content=request.query)])
            return {"respnse":response.content}
        except Exception as e:
            raise HTTPException(status_code=500,detail=str(e))
