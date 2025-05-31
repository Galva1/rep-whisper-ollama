# 🎧 Transcrição e Resumo de Áudio com Whisper e Ollama

Este projeto realiza a **transcrição de um arquivo de áudio** utilizando o modelo `Whisper` da OpenAI e, em seguida, envia o texto transcrito para o **Ollama** (modelo de linguagem local) para gerar um **resumo automático**. É uma ferramenta simples e eficaz para automatizar a extração de conteúdo falado e sua condensação em formato de texto.

---

## 🛠️ Requisitos de Instalação

### 📦 Whisper

Instale o pacote Whisper usando `pip`:

```bash
pip install -U openai-whisper
```

Ou diretamente do repositório oficial:

```bash
pip install git+https://github.com/openai/whisper.git
```

### 📼 FFmpeg

Whisper depende do FFmpeg para processar arquivos de áudio.

#### 🪟 Windows (com Chocolatey)

1. Instale o [Chocolatey](https://chocolatey.org/install):
   - Abra o PowerShell como administrador.
   - Execute:

   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force;
   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
   iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

2. Com o Chocolatey instalado, instale o FFmpeg:

   ```bash
   choco install ffmpeg
   ```

#### 💡 Verificação

Após a instalação, verifique se o FFmpeg está acessível via terminal:

```bash
ffmpeg -version
```

---

## 🤖 Ollama

Este projeto também utiliza o [Ollama](https://ollama.com/) para gerar resumos locais com modelos como `llama3`, `mistral`, etc.

1. Baixe e instale o Ollama em: https://ollama.com/download  
2. Rode o modelo desejado (exemplo com Mistral):

```bash
ollama run mistral
```

---

## ▶️ Como Executar o Script

1. Coloque seu arquivo de áudio (ex: `audio.mp3`) no local desejado.
2. Edite o caminho no script Python para apontar corretamente para seu arquivo.
3. Execute o script:

```bash
python transcrever_resumir.py
```

---

## 💡 Exemplo de Uso

Pode-se ser usado para transcrever áudios, reuniões gravadas, chaveando os pontos importantes de forma prática e rápida.

## 📄 Licença

Este projeto é de uso livre para fins educacionais e experimentais.

---

## 🙋‍♂️ Dúvidas?

Se precisar de ajuda para instalar o Ollama, configurar seu ambiente ou adaptar o código, sinta-se à vontade para abrir uma issue ou contribuir!
