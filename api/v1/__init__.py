from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.v1.Config import Config
from api.v1.database.db import init_db

def build_api():
    api = FastAPI(debug=Config.debug)

    @api.on_event("startup")
    async def start_db():
        await init_db()

    @api.get("/")
    async def get_docs():
        return RedirectResponse("/docs")

    return api