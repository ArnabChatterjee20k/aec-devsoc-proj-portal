from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from Config import Config
from database.db import init_db

api = FastAPI(debug=Config.debug)

@api.on_event("startup")
async def start_db():
    await init_db()

@api.get("/")
async def get_docs():
    return RedirectResponse("/docs")

if __name__ == "__main__":
    uvicorn.run("app:api", reload=Config.debug)