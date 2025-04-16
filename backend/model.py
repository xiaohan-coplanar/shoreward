from pydantic import BaseModel, Field
from typing import Literal
from datetime import date

class TravelPlanRequest(BaseModel):
    current_city: str = Field(..., example="New York")
    destination_city: str = Field(..., example="Tokyo")
    start_date: date = Field(..., example="2025-07-01")
    end_date: date = Field(..., example="2025-07-14")
    budget_level: Literal["super budget", "midclass", "luxury"] = Field(..., example="midclass")