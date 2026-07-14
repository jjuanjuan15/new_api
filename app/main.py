from fastapi import FastAPI, HTTPException, Query, Depends, Header
import os
from services.service import funcion_elisa,funcion_putos
from huggingface_hub import InferenceClient

app = FastAPI()

client = InferenceClient(
    provider="hf-inference",
    api_key="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"
)
app = FastAPI()

PASSWORD = os.getenv("PSW", "putogordo12")

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
@app.get("/puto", dependencies=[Depends(comprobar_password)])
async def putos():
    return await funcion_putos()
@app.get("/ia")
async def ia(prompt: str):
    respuesta = client.chat.completions.create(
        model="HuggingFaceTB/SmolLM2-135M-Instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )

    return {
        "respuesta": respuesta.choices[0].message.content
    }
