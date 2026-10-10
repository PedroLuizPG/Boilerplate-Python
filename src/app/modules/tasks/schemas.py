from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    done: bool | None = None
    
class TaskRead(BaseModel):
    # from_attributes=True permite criar o schema a partir de um objeto do SQLAlchemy
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    title: str
    done: bool
    created_at: datetime