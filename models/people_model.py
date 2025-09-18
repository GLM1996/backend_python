import httpx
import base64
from utils import config
from database import db  # importamos la base de datos ya conectada

apiKey = config.API_KEY_JC
urlBase = "https://api.followupboss.com/v1/people"
collection = db.peoples  # Colección para personas


async def getPeopleById(id: int):
    url = f"{urlBase}/{id}"

    # Crear header Authorization Basic
    encoded = base64.b64encode(f"{apiKey}:".encode()).decode()
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Basic {encoded}",
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()  # lanza error si el status no es 200
            data = response.json()  # parsear la respuesta como JSON
            return {"message": "Lista de personas", "id": id, "data": data}

    except httpx.HTTPStatusError as e:
        return {"error": f"Error en la API externa: {e.response.status_code}"}
    except Exception as e:
        return {"error": str(e)}


async def getPeopleByIdDb(id: int):
    person = await collection.find_one({"id": id})
    if person:
        return person
    return {"message": "No se encontró la persona con ese id"}
