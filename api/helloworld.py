from fastapi import APIRouter

router = APIRouter()
prefix = "/helloworld"

@router.get("/")
async def root():
    return {"message": "Hello World"}