from fastapi import APIRouter
from controllers.people_controller import searchPeopleById
from controllers.people_controller import searchPeopleByIdDb   

router = APIRouter()    

@router.get("/people/{id}") # desde follow
async def get_people(id: int):
    people = await searchPeopleById(id)  # usar await
    return {"people": people}

@router.get("/peopleMongo/{id}") # desde mongo
async def get_people(id: int):
    people = await searchPeopleByIdDb(id)  # usar await
    return {"people": people}