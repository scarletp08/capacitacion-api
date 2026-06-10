from fastapi import FastAPI, Request
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
async def formulario(request: Request):
    data = await request.json()

    print(data)

    return {
        "recibido": data
    }
