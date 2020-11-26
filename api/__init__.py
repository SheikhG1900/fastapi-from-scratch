from fastapi import APIRouter
from api import helloworld

def api_router():
    router = APIRouter()
    router.include_router(helloworld.router, prefix=helloworld.prefix)
    return router 