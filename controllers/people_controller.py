from models.people_model import getPeopleById
from models.people_model import getPeopleByIdDb
from utils.serializer import serialize_mongo_doc

async def searchPeopleById(id: int):
    people = await getPeopleById(id)    
    if "error" in people:
        return people  # Retorna el error si ocurrió
    return {"message": "Lista de personas", "id": id,"people": people}

async def searchPeopleByIdDb(id: int):
    people = await getPeopleByIdDb(id)
    if people and isinstance(people, dict):
        people = serialize_mongo_doc(people)  # Serializar el documento
    if "error" in people:
        return people  # Retorna el error si ocurrió
    return people