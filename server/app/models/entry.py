from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class EntryIn(BaseModel):
    """Journal entry input"""
    mood: int = Field(..., ge=1, le=5, description="Mood rating 1-5")
    note: str = Field(..., min_length=1, max_length=1000)

class EntryOut(BaseModel):
    """Journal entry output"""
    id: str
    mood: int
    note: str
    createdAt: datetime
    userId: Optional[str] = None

