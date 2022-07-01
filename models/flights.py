from pydantic import BaseModel, Field


class Flight(BaseModel):
    arrival: str = Field(alias="Arrival")
    departure: str = Field(alias="Departure")
    success: str = Field(alias="success")

    class Config:
        allow_population_by_field_name = True
