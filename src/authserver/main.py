from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/auth")
async def auth(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=403, detail="Authorization header missing")
    return {"message": "Authorized!"}


@app.get("/", response_class=HTMLResponse)
async def read_root():
    content = "<html><body><h1>Hello, world!</h1></body></html>"
    headers = {"X-Custom-Header": "Value", "Cache-Control": "no-store"}
    return HTMLResponse(content=content, headers=headers)
