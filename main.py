from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Conexión MongoDB Atlas
client = MongoClient(
    "mongodb+srv://prueba:ZA5DjJgHLMxLivDNK@cluster0.p2djwko.mongodb.net/?appName=Cluster0"
   
)

db = client["capacitacion"]

collection = db["formularios"]

@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando"
    }


@app.post("/formulario")
def formulario(data: dict):

    resultado = collection.insert_one(data)

    return {
        "ok": True,
        "id": str(resultado.inserted_id)
    }


