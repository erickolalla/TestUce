import openai
import os
import openai
from dynapat import BaseModel
from fastapi import FastApi


app = FastApi()

class openia(BaseModel):
    promt: str

class hostlocal(BaseModel):
    lc: int

hostlocal("1015")

@app.post("/bn")
def endpoint(promt: str) -> list:
    openai.organization = "org-PukKJ0lEU2b0jyEJplPr0m80"
    openai.API_key = "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" #token generado con mi cuenta personal erickfabri.01@gmail.com ya que presentaba errores con la cueta institucional
    messages = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": """Eres un asistente para poder convertir números a formato binario, debes respoder correctamente a la petición que se te pida
        E.G = 4
        - Tu número binario es 100 """},
                     {"role": "user", "content": "!"}]
    }
    return promt.choice[0].promt.response[0]
    return promt.usage.tokens.response[1]

