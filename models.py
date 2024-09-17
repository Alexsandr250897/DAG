from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Task(BaseModel):
    id: str
    name: str
    command: str
    dependencies: Optional[List[str]] = []

class DAG(BaseModel):
    tasks: List[Task]
