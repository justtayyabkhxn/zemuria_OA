from fastapi import FastAPI
from langflow.api.health_check_router import health_check_router
from langflow.api.log_router import log_router
from langflow.api.router import router
from langflow.api.routes  import custom_query

app = FastAPI()

from fastapi import APIRouter
from langflow.api.v1 import router as v1_router

router = APIRouter()
router.include_router(v1_router, prefix="/api/v1")


app.include_router(custom_query.router)
__all__ = ["health_check_router", "log_router", "router"]
