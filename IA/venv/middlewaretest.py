from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware( 
    CORSMiddleware,
    allow_origins="http://localhost:5173",
    allow_credentials=True
    allow_methods=["*"]
    allow_methods=["*"]
)

class TextRequest(BaseModel):
    Text: str

@app.post("/")
def read_root(request: TextRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="alguma coisa deu errado")
   
   
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