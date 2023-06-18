from os import environ
from dotenv import load_dotenv
load_dotenv(".env")
class Config:
    env = environ.get("ENV")
    debug = False if env=="PROD" else True
    db_uri = environ.get("DB_URI")