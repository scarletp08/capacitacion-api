from fastapi import FastAPI, Request
from pymongo import MongoClient

app = FastAPI()

MONGO_URI = "mongodb+srv://prueba:ZA5DjJgHLMxLivDNK@cluster0.p2djwko.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

db = client["capacitacion"]
collection = db["formularios"]

@app.post("/formulario")
async def formulario(request: Request):

    data = await request.json()

    print("DATA RECIBIDA:", data)

    resultado = collection.insert_one(data)

    print("INSERTADO:", resultado.inserted_id)

    return {
        "mensaje": "Guardado",
        "id": str(resultado.inserted_id)
    }
    
  
