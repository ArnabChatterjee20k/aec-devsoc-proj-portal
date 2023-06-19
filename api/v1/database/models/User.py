from beanie import Document , Link
from typing import Optional

class User(Document):
    name:str
    profile_id : str
    email : str
    profession : list[str]
    institution:str

    password : str #hashed()

    # automatically created
    contributed: Optional[list]