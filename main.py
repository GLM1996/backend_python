from fastapi import FastAPI
from database import db  # importamos la base de datos ya conectada
from routes.people_route import router as people_router 

app = FastAPI()
app.include_router(people_router)

# Ejemplo: ruta raíz
@app.get("/")
def read_root():
    return {"message": "Hola Mundo"}


