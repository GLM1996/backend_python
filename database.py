from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from utils import config
import sys

# Función para conectar a MongoDB
def connect_db(uri=config.MONGO_URI_JC):
    try:
        client = MongoClient(uri)        
        print("✅ Conectado a MongoDB")
        return client
    except Exception as e:
        print("❌ Error conectando a MongoDB:", e)
        sys.exit(1)  # Detener el proceso si hay error

# Conectar
client = connect_db()
# Seleccionar base de datos
db = client["backend"]
