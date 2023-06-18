from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from Config import Config

api = FastAPI(debug=Config.debug)

@api.get("/")
def get_docs():
    return RedirectResponse("/docs")

if __name__ == "__main__":
    uvicorn.run("app:api",reload=Config.debug)