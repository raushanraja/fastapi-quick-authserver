import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()


@app.get("/")
async def read_root(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=403, detail="Authorization header missing")
    return {"message": "Authorized!"}
