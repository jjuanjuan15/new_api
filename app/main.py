from fastapi import FastAPI, HTTPException, Query, Depends, Header
import os
from services.service import funcion_elisa
app = FastAPI()

PASSWORD = os.getenv("PSW")

API_KEY = "3e8d7f1c8b9a4f2e6d5a1b7c9e8f4a2d"
def comprobar_password(password: str = Query(...)):
    if password != PASSWORD:
        raise HTTPException(status_code=401, detail="No autorizado")

@app.get("/")
def inicio(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401)
    return {"message": "Hola"}

@app.get("/usuarios", dependencies=[Depends(comprobar_password)])
def usuarios():
    return ["Juan", "Ana"]

@app.get("/elisa", dependencies=[Depends(comprobar_password)])
async def elisa():
    return await funcion_elisa()