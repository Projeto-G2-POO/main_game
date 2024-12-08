from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
import threading
import tkinter as tk
import requests # type: ignore
import uvicorn
import ollama
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/submit/")
# ...

def enviar_texto():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        resultado_label.config(text="Por favor, insira um texto.")
        return
    
    
    def chamar_api():
        try:
            
            contexto = "You are a RPG master Narrator. you know everything about a RPG lore, universe and characters"
            
            
            mensagens = [
                {"role": "system", "content": contexto},
                {"role": "user", "content": texto}
            ]
            
            
            if len(mensagens) > 5:  
                mensagens = mensagens[-5:]  

            response = requests.post("http://127.0.0.1:8000/submit/", json={"text": str(mensagens)})
            if response.status_code == 200:
                resposta = response.json().get("resposta", "Nenhuma resposta recebida.")
                resultado_label.config(text=f"Resposta da IA: {resposta}")
            else:
                resultado_label.config(text=f"Erro: {response.json().get('detail', 'Erro desconhecido')}")
        except Exception as e:
            resultado_label.config(text=f"Erro ao conectar: {str(e)}")

    
    threading.Thread(target=chamar_api, daemon=True).start()




def iniciar_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)


def enviar_texto():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        resultado_label.config(text="null / nada preenchido")
        return
    
    try:
        response = requests.post("http://127.0.0.1:8000/submit/", data={"text": texto})
        if response.status_code == 200:
            resposta = response.json().get("resposta", "Nenhuma resposta recebida.")
            resultado_label.config(text=f"Resposta da IA: {resposta}")
        else:
            resultado_label.config(text=f"Erro: {response.json().get('detail', 'Ocorreu um erro...:(')}")
    except Exception as e:
        resultado_label.config(text=f"Erro ao conectar: {str(e)}")


threading.Thread(target=iniciar_api, daemon=True).start()


#janela do app-------------------------------------------------------------------------------------------------------------------------------

def iniciar_arraste(event):
    global posicao_inicial
    posicao_inicial = event.x, event.y

def arrastar_botao(event):
    global posicao_inicial
    delta_x = event.x - posicao_inicial[0]
    delta_y = event.y - posicao_inicial[1]

    nova_largura = entrada_texto.winfo_width() + delta_x
    nova_altura = entrada_texto.winfo_height() + delta_y

    if nova_largura > 100 and nova_altura > 50:  
        entrada_texto.config(width=nova_largura // 10, height=nova_altura // 20)
    posicao_inicial = event.x, event.y

janela = tk.Tk()
janela.title("Interface para IA")
janela.configure(bg="#1E1E1E")  


frame_principal = tk.Frame(janela, bg="#1E1E1E")
frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

label = tk.Label(frame_principal, text="Insira o texto:", bg="#1E1E1E", fg="white", font=("Arial", 14))
label.pack(pady=(0, 10))

entrada_texto = tk.Text(frame_principal, height=5, width=50, bg="#2A2A2A", fg="white", insertbackground="white", borderwidth=2, relief="solid", font=("Arial", 12))
entrada_texto.pack(pady=(0, 10))

botao_enviar = tk.Button(frame_principal, text="Enviar", command=enviar_texto, bg="#4D4D4D", fg="white", font=("Arial", 12), borderwidth=0, padx=10, pady=5)
botao_enviar.pack(pady=5)


botao_redimensionar = tk.Frame(frame_principal, bg="#4D4D4D", width=10, height=10)
botao_redimensionar.pack(side=tk.RIGHT, anchor=tk.SE, padx=(0, 5), pady=(0, 5))


botao_redimensionar.bind("<Button-1>", iniciar_arraste)
botao_redimensionar.bind("<B1-Motion>", arrastar_botao)

resultado_label = tk.Label(frame_principal, text="", bg="#1E1E1E", fg="white", wraplength=450, justify="center", font=("Arial", 12))
resultado_label.pack(pady=10)

janela.mainloop()