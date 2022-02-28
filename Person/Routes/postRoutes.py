# FastAPI
from fastapi import Body
from fastapi import APIRouter


from ..Classes.personClass import Person, PersonOut
router = APIRouter()


@router.post("/person/new", tags=["Person"], response_model=PersonOut)
def create_person(person: Person = Body(...)):
    return person
