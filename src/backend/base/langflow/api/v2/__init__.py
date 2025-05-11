from fastapi import FastAPI
from langflow.api.v2.files import router as files_router

__all__ = [
    "files_router",
]

from fastapi import APIRouter
from . import openai

router = APIRouter()
router.include_router(openai.router, prefix="/openai", tags=["openai"])

from langflow.api.router import router
from langflow.api.routes  import custom_query

app = FastAPI()

app.include_router(custom_query.router)
