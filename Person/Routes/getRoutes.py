# Python
from typing import Optional


# FastAPI
from fastapi import Query, Path
from fastapi import APIRouter

router = APIRouter()

# Validaciones: Query Parameters

@router.get("/person/detail", tags=["Person"])
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


@router.get(path="/person/detail/{person_id}", tags=["Person"])
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
