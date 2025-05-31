import whisper
import requests

model = whisper.load_model("base") # Carregando o modelo Whisper
caminho_correto = r"C:\audio.mp3" # Substitua pelo caminho correto do seu arquivo de áudio
result = model.transcribe(caminho_correto) # Transcrevendo o áudio
texto = result["text"] # Armazenando o texto transcrito
print(texto) # Exibe o texto transcrito

prompt = f"Resuma brevemente o seguinte texto:\n\n{texto}, trazendo os principais pontos chaves." # Enviando o texto para a API de resumo

resposta = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral", # Modelo de linguagem a ser utilizado
        "prompt": prompt,
        "stream": False
    }
) # Verificando se a resposta foi bem-sucedida

resumo = resposta.json()["response"]
print("Resumo:\n", resumo) # Exibe o resumo