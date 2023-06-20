from pydantic import BaseModel


class ProjectOwnerSchema(BaseModel):
    profile_id: str
