from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from pymongo import MongoClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
MONGO_URI = "mongodb+srv://prueba:tWdYsznMmn5yZ8BQ@cluster0.p2djwko.mongodb.net/?appName=Cluster0"


client = MongoClient(MONGO_URI)

db = client["capacitacion"]
collection = db["formularios"]

@app.post("/formulario")
async def formulario(request: Request):

    data = await request.json()

    print(data)

    resultado = collection.insert_one(data)

    print("INSERTADO:", resultado.inserted_id)

    return {
        "mensaje": "Guardado correctamente",
        "id": str(resultado.inserted_id)
    }

@app.get("/dashboard/respuestas")
async def respuestas():

    data = list(collection.find({}, {"_id": 0}))

    return data

@app.get("/test")
async def test():

    collection.insert_one({
        "test": "ok"
    })

    return {"ok": True}