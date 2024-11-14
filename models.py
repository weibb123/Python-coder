from pydantic import BaseModel, Field
from typing import Optional

class QueryInput(BaseModel):
    query: str
    temperature: Optional[float] = Field(default=0.0, ge=0.0, le=1.0)

class QueryResponse(BaseModel):
    response: str
    model_used: str