Chatbot Python com LangChain + OpenAI GPT-4

Um chatbot de linha de comando especializado em responder perguntas sobre programação em Python, desenvolvido utilizando:

LangChain → Orquestração e pipeline conversacional

OpenAI GPT-4 / GPT-4o / GPT-4o-mini → LLM para respostas

LangSmith (opcional) → Observabilidade, tracing e debugging de prompts

Clean Code + Testes + Estrutura modular

Ideal como base para:

Chatbots educativos

Sistemas internos de ajuda

Provas de conceito com arquiteturas LLM

📦 1. Requisitos
✔ Softwares necessários
Item	Versão Requerida
Python	3.10+
pip	Atualizado
Git	Opcional
Conta na OpenAI	Obrigatória
Conta no LangSmith	Opcional
🔐 2. Criando sua conta e API Key da OpenAI
👉 Passo 1 — Criar sua conta

Acesse:
https://platform.openai.com

Clique em Sign Up e siga o cadastro.

👉 Passo 2 — Gerar uma API Key

Entre em https://platform.openai.com/settings/organization/api-keys

Clique em Create new secret key

Nomeie como quiser (ex.: chatbot-python)

Copie a chave (não é exibida novamente!)

Exemplo de chave (NUNCA coloque isso real no GitHub):

sk-9nJH3hdjasd-EXEMPLO-123456

⚠ Atenção

Nunca compartilhe sua API Key.

Nunca suba .env para o GitHub.

Use .gitignore adequadamente.

📊 3. (Opcional) Criando conta e API Key no LangSmith

LangSmith fornece:

Tracing completo de chains

Análise de conversas

Métricas de custo e latência

Debug de prompts

👉 Passo 1 — Criar conta

https://smith.langchain.com/

👉 Passo 2 — Criar API Key

Acesse: Settings → API Keys

Clique em Create API Key

Copie a chave

Configure no .env

📁 4. Estrutura do Projeto
chatbot-python-llm/
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

⚙️ 5. Instalação e Configuração
🧩 5.1 Clonar o projeto
git clone https://github.com/<seu-usuario>/<seu-repo>.git
cd chatbot-python-llm

🐍 5.2 Criar ambiente virtual
Windows (PowerShell)
python -m venv .venv
.venv\Scripts\activate

Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

📦 5.3 Instalar dependências
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

🔧 5.4 Criar arquivo .env

Copie o modelo:

cp .env.example .env


Edite com suas chaves:

OPENAI_API_KEY=coloque_sua_key_aqui
OPENAI_MODEL=gpt-4o-mini

# Opcional: LangSmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=sua_chave_langsmith
LANGCHAIN_PROJECT=python-chatbot


❗ O arquivo .env NUNCA deve ser commitado.

▶️ 6. Executando o Chatbot
Windows
python -m src.main

Linux / macOS
python3 -m src.main

🧪 Exemplo de uso

Você digita:

Como criar uma lista em Python?


Chatbot responde:

Para criar uma lista em Python, use colchetes:

```python
frutas = ["maçã", "banana", "uva"]
print(frutas)


Listas são mutáveis e permitem operações como append(), remove(), etc.


---

# 🧪 **7. Rodando Testes**

Antes, garanta que o `src` está no `PYTHONPATH`:

### Windows

```powershell
$env:PYTHONPATH = (Resolve-Path .\src).Path
pytest -q

Linux/macOS
export PYTHONPATH=$(pwd)/src
pytest -q

🛡️ 8. Boas Práticas Adotadas

✔ Arquitetura limpa
✔ Classes separadas por responsabilidade
✔ Histórico de conversas estruturado
✔ LangChain + OpenAI via langchain-openai
✔ Testes com LLM Fake (rápidos e determinísticos)
✔ .env seguro
✔ Tipagem forte com Python
✔ Suporte opcional a LangSmith para observabilidade

📈 9. Possíveis Extensões Futuras

Interface Web com FastAPI

API REST para chatbot

Cache de respostas

Memória persistente em banco

Logs estruturados (Elastic / Datadog)

Modo streaming da OpenAI

Modo multimodal (imagens + texto)