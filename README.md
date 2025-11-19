# 🤖 Chatbot Python com LangChain + OpenAI (GPT-4 / GPT-4o)

Um chatbot de **linha de comando** especializado em responder perguntas sobre programação em **Python**, desenvolvido com:

- **LangChain** → Orquestração e pipeline conversacional  
- **OpenAI GPT-4 / GPT-4o / GPT-4o-mini** → Modelo de linguagem  
- **LangSmith** (opcional) → Observabilidade, tracing e depuração  
- **Clean Code**, **estrutura modular** e **testes automatizados**

Ideal para:

- Chatbots educacionais  
- Ferramentas internas de suporte  
- POCs com LLMs  
- Projetos que exigem rastreabilidade e boas práticas  


---

# 📦 1. Requisitos

| Item | Versão |
|------|--------|
| **Python** | 3.10+ |
| **pip** | Atualizado |
| **Git** | Opcional |
| **Conta na OpenAI** | Obrigatória |
| **Conta no LangSmith** | Opcional |


---

# 🔐 2. Criando sua conta e API Key da OpenAI

### 👉 Passo 1 — Criar conta  
Acesse: https://platform.openai.com

### 👉 Passo 2 — Gerar API Key  
Acesse: https://platform.openai.com/settings/organization/api-keys  

Clique em **Create new secret key**.

> ❗ **Nunca coloque sua chave real no GitHub.**

Exemplo fictício:

```
sk-EXEMPLO-123456789
```

### ⚠ Boas práticas
- Nunca compartilhe sua API Key  
- Nunca faça commit do `.env`  
- Use `.gitignore` corretamente  


---

# 📊 3. (Opcional) Configurando LangSmith

O LangSmith permite:

- Tracing das chains  
- Métricas de custo e latência  
- Debug de prompts  

### Criar conta  
https://smith.langchain.com/

### Criar API Key  
Settings → **API Keys** → *Create API Key*

Adicionar ao `.env`:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=sua_key
LANGCHAIN_PROJECT=python-chatbot
```


---

# 📁 4. Estrutura do Projeto

```
chatbot_ia/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── chatbot.py
│   └── main.py
│
├── tests/
│   ├── conftest.py
│   └── test_chatbot.py
│
├── .env.example
├── requirements.txt
└── README.md
```


---

# ⚙️ 5. Instalação e Configuração

## 🧩 5.1 Clonar o repositório

```bash
git clone https://github.com/<seu-usuario>/<seu-repo>.git
cd chatbot_ia
```

## 🐍 5.2 Criar ambiente virtual

### Windows
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 📦 5.3 Instalar dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 🔧 5.4 Criar arquivo `.env`

Copie o modelo:

```bash
cp .env.example .env
```

Edite:

```
OPENAI_API_KEY=sua_key
OPENAI_MODEL=gpt-4o-mini

# opcional LangSmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=sua_key_langsmith
LANGCHAIN_PROJECT=python-chatbot
```

> ❗ O `.env` **nunca deve ser commitado**.


---

# ▶️ 6. Executando o Chatbot

### Windows

```powershell
python -m src.main
```

### Linux/macOS

```bash
python3 -m src.main
```


---

# 💬 Exemplo de uso

Entrada:

```
Como criar uma lista em Python?
```

Saída:

```
Para criar uma lista em Python, utilize colchetes:

frutas = ["maçã", "banana", "uva"]
print(frutas)

Listas são mutáveis e possuem métodos como append(), remove(), etc.
```


---

# 🧪 7. Rodando Testes

Antes, configure o **PYTHONPATH**.

### Windows
```powershell
$env:PYTHONPATH = (Resolve-Path .\src).Path
pytest -q
```

### Linux / macOS
```bash
export PYTHONPATH=$(pwd)/src
pytest -q
```


---

# 🛡️ 8. Boas práticas adotadas

✔ Arquitetura limpa (Clean Code)  
✔ Separação clara de responsabilidades  
✔ Histórico de conversas estruturado  
✔ LangChain + OpenAI via `langchain-openai`  
✔ Testes com LLM Fake (determinísticos e rápidos)  
✔ Variáveis sensíveis isoladas em `.env`  
✔ Tipagem forte (Python typing)  
✔ Suporte opcional ao LangSmith  


