# Python
from typing import Optional
from enum import Enum


# Pydantic
from pydantic import BaseModel
from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Models


class HeairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blone"
    red = "red"


class Person(BaseModel):
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
    hair_color: Optional[HeairColor] = Field(default=None, example="Brown")
    is_married: Optional[bool] = Field(default=None, exampple="True")

    """class Config:
        schema_extra = {
            "example": {
                "first_name": "Julián",
                "last_name": "Melero",
                "age": 38,
                "hair_color": "brown",
                "is_married": True
            }
        }"""


class Location(BaseModel):
    city: str = Field(example="València")
    state: str = Field(example="València")
    country: str = Field(example="Spain")


@app.get("/", status_code=200)
def home():
    return {
        "Hello": "World"
    }

# Request and Response


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, min_length=1,
        max_length=50,
        title="Person Name",        
        description="This is the person name. Between 1 and 50 characters",
        example="Pepe"
    ),
    age: Optional[int] = Query(
        ...,
        gt=17,
        title="Person Age",
        description="This is the person age. Required.",
        example=25
    )
):
    return {name: age}

# Validaciones: PAth Parameteres


@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID. Required",
        example=123
    )
):
    return {person_id: "It exists!"}

# Validaciones: Request Body


@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID.",
        gt=0,
        example=123
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results
