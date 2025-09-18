from bson import ObjectId
from typing import Any, Dict, List

def serialize_mongo_doc(doc: Any) -> Any:
    """
    Convierte documentos de MongoDB a JSON serializable para FastAPI.
    Convierte ObjectId a str de forma recursiva en dicts y listas.
    """
    if isinstance(doc, list):
        return [serialize_mongo_doc(item) for item in doc]
    elif isinstance(doc, dict):
        serialized = {}
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                serialized[key] = str(value)
            else:
                serialized[key] = serialize_mongo_doc(value)
        return serialized
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc
