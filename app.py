from fastapi import FastAPI
import uvicorn
from Config import Config

api = FastAPI(debug=Config.debug)

if __name__ == "__main__":
    uvicorn.run("app:api",reload=Config.debug)