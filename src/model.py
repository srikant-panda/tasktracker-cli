from pydantic import BaseModel,Field
from uuid import UUID , uuid4
from typing import Literal
from datetime import date
class Base(BaseModel):
    pass

class TaskModel(Base):
        id : UUID = Field(
            default_factory=uuid4,
            title= "task id",
            description="A unique id to evry task."
        )

        description : str
        status : Literal['todo','done','in-progress'] = Field(default='todo')
        created_at : date = Field(
            default= date.today()
        )
