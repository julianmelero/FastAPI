# from .dependencies import FastAPI, Body,Path
from logging import root
from sys import prefix
from fastapi import APIRouter, FastAPI
from fastapi import Body, Query, Path, status

# Person Classes
from Person.Classes.personClass import Person,Location


# Routes
from Person.Routes import routes


app = FastAPI()
# app.mount("/api/v1",  app)
app.include_router(routes.router,prefix="/api/v1")
app.include_router(routes.router, prefix="/api/v1")



@app.get("/", tags=["General"], status_code=status.HTTP_200_OK)
def home():
    return ({
        "name": "World"
    })



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
