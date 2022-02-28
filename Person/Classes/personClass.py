# Python
from typing import Optional
from enum import Enum


# Pydantic
from pydantic import BaseModel
from pydantic import Field





class HeairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blone"
    red = "red"


class PersonBase(BaseModel):
    first_name: str = Field(
            ...,
            min_length=1,
            max_length=50,
            example="Julián"
        )
    last_name: str = Field(
            ...,
            min_length=1,
            max_length=50,
            example="Melero"
        )
    age: int = Field(
            ...,
            gt=0,
            lt=115,
            example=38
        )
    hair_color: Optional[HeairColor] = Field(default=None, example="brown")
    is_married: Optional[bool] = Field(default=None, exampple="True")



class Person(PersonBase):
    password: str = Field(..., min_length=8)




class PersonOut(PersonBase):
    pass


class Location(BaseModel):
    city: str = Field(example="València")
    state: str = Field(example="València")
    country: str = Field(example="Spain")
