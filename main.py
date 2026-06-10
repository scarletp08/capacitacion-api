from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Conexión MongoDB Atlas
client = MongoClient(
    "mongodb+srv://prueba:ZA5DjJgHLMxLivDNK@cluster0.p2djwko.mongodb.net/?retryWrites=true&w=majority"
  
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
    try:
        resultado = collection.insert_one(data)
        print("INSERT OK:", resultado.inserted_id)

        return {
            "ok": True,
            "id": str(resultado.inserted_id)
        }

    except Exception as e:
        print("ERROR MONGO:", str(e))

        return {
            "ok": False,
            "error": str(e)
        }
