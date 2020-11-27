from fastapi import APIRouter

router = APIRouter()
prefix = "/examples"

@router.get("/helloworld")
async def root():
    return {"message": "Hello World"}


@router.get("/path/{slug:path}")
async def path(slug:str):
    return {"path": slug}