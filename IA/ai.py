#$response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/" -Method POST -Headers @{
#>>     "Content-Type" = "application/json"
#>> } -Body '{"text": "answer accordingly: imagine you are on a medieval world, in a grass field, 
#you are a traveler venturing from afar, answer propperly: imagine you are a goblin standing by my side, 
#give a warm welcome to the  traveller. remember, we are in a open gras field, with monsters arriving soon."}'

#uvicorn ---ai:app --reload---  starta o server e deixa ele atualizar em tempo real
# ---$response.content---     mostra a resposta da llm inteira









from fastapi import FastAPI, HTTPException 
import ollama
from pydantic import BaseModel 


app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/")
def read_root(request: TextRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="não funcionou")

    try:
        response = ollama.chat(model="tinyllama", messages=[
            {
                 "role": "user",
                 "content": request.text
            }
        ])
        llm_res = response.get('message', {}).get('content', '')

        return {"resposta do LLM:": llm_res} 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   
