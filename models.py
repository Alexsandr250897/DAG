from pydantic import BaseModel
from typing import List, Optional

class Task(BaseModel):
    id: str
    name: str
    command: str
    dependencies: Optional[List[str]] = []

class DAG(BaseModel):
    tasks: List[Task]
