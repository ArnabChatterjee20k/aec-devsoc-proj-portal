import uvicorn
from api.v1 import build_api, Config
api = build_api()
if __name__ == "__main__":
    uvicorn.run("app:api", reload=Config.debug)
