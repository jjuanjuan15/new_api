from fastapi import FastAPI, HTTPException, Query, Depends, Header
from fastapi.responses import FileResponse, StreamingResponse
import os
import io
from services.service import funcion_elisa,funcion_putos
import qrcode


app = FastAPI()

PASSWORD = os.getenv("PSW")

API_KEY = os.getenv("API_KEY")
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
@app.get("/puto", dependencies=[Depends(comprobar_password)])
async def putos():
    return await funcion_putos()
@app.get("/genqr")
async def genqr(url: str):
    img = qrcode.make(url)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")