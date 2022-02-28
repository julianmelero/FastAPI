# from .dependencies import FastAPI, Body,Path
from fastapi import FastAPI
from fastapi import Body, Query, Path, status

# Person Classes
from Person.Classes.personClass import Person,Location


# Routes
from Person.Routes import getRoutes,postRoutes


app = FastAPI()


app.include_router(getRoutes.router)
app.include_router(postRoutes.router)



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
