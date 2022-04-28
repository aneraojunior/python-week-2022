from typing import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator

class Beer(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    name: str
    style: str
    flavor: int
    image: int
    cost: int

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
            return v

try:
    brewdog = Beer(name="Brewdog", style="Neipa", flavor=9, image=8, cost=6)
except RuntimeError:
    print("Zika de mais")