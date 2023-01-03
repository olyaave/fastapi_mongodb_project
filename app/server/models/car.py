from typing import Optional

from pydantic import BaseModel, Field


class CarSchema(BaseModel):
    brand: str = Field(...)
    series: str = Field(...)
    color: str = Field(...)
    year_of_release: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "brand": "BMW",
                "series": "M3",
                "color": "Blue",
                "year_of_release": "2016",
            }
        }


class UpdateCarModel(BaseModel):
    brand: Optional[str]
    series: Optional[str]
    color: Optional[str]
    year_of_release: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "brand": "BMW",
                "series": "M5",
                "color": "Yellow",
                "year_of_release": "2020",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}