#Python
from typing import Optional
from fastapi.param_functions import Query, Path

#Pydantic
from pydantic import BaseModel


# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


class Location(BaseModel):
    city: str
    state: str
    country: str


@app.get("/")
def home():
    return {
        "Hello" : "World"
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
        title= "Person Name",
        description="This is the person name. Between 1 and 50 characters"
        ),
    age: Optional[int] = Query(
        ...,
        gt=17,
        title="Person Age",
        description="This is the person age. Required."
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
        description="This is the person ID. Required"
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
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results