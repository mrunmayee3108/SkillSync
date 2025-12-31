from pydantic import BaseModel
from typing import List

class bulkskillCreate(BaseModel):
    skill_req: List[str]