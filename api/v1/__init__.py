from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.v1.Config import Config
from api.v1.database.db import init_db
from api.v1.routes.user import user
from api.v1.routes.auth import auth

def build_api():
    api = FastAPI(debug=Config.debug)

    @api.on_event("startup")
    async def start_db():
        await init_db()
        print("started")
        

    @api.get("/")
    async def get_docs():
        return RedirectResponse("/docs")

    api.include_router(user.router,prefix="/users")
    api.include_router(auth.router,prefix="/auth")

    return api