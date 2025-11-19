🤖 Chatbot Python com LangChain + OpenAI (GPT-4 / GPT-4o)

Um chatbot de linha de comando especializado em responder perguntas sobre programação em Python, desenvolvido com foco em:

LangChain → Orquestração, prompts e pipeline conversacional

OpenAI GPT-4 / GPT-4o / GPT-4o-mini → LLM para respostas

LangSmith (opcional) → Observabilidade, tracing e depuração

Clean Code + Estrutura modular + Testes automatizados

Ideal para:

Chatbots educacionais

Ferramentas internas de suporte

Estudos e POCs com arquiteturas baseadas em LLM

Projetos que exigem rastreabilidade e boas práticas

📦 1. Requisitos
Item	Versão
Python	3.14
pip	Atualizado
Git	Opcional
Conta na OpenAI	Obrigatória
Conta no LangSmith	Opcional
🔐 2. Criando sua conta e API Key da OpenAI
👉 Passo 1 — Criar uma conta

Acesse: https://platform.openai.com

Clique em Sign Up e finalize o cadastro.

👉 Passo 2 — Gerar uma API Key

Acesse:
https://platform.openai.com/settings/organization/api-keys

Clique em Create new secret key
Nomeie como quiser (ex.: chatbot-python)
Copie a chave — ela não será exibida novamente.

❗ Nunca coloque sua chave real no GitHub.

Exemplo fictício:

sk-EXEMPLO-123456789

⚠ Boas práticas

Nunca compartilhe sua API Key

Nunca envie .env para o repositório

Utilize .gitignore corretamente

📊 3. (Opcional) Configurando LangSmith

O LangSmith fornece:

Tracing completo das chains

Métricas de custo e latência

Histórico de conversas

Debug de prompts

👉 Criar conta

https://smith.langchain.com/

👉 Criar API Key

Settings → API Keys → Create API Key

Adicionar ao .env:

LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=sua_key
LANGCHAIN_PROJECT=python-chatbot

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
🧩 5.1 Clonar o repositório
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


Edite:

OPENAI_API_KEY=sua_key
OPENAI_MODEL=gpt-4o-mini

# opcional
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=sua_key_langsmith
LANGCHAIN_PROJECT=python-chatbot


❗ O .env nunca deve ser commitado.

▶️ 6. Executando o Chatbot
Windows
python -m src.main

Linux / macOS
python3 -m src.main

💬 Exemplo de uso

Você digita:

Como criar uma lista em Python?


O chatbot responde:

Para criar uma lista em Python, utilize colchetes:

frutas = ["maçã", "banana", "uva"]
print(frutas)

Listas são mutáveis e permitem métodos como append(), remove(), etc.

🧪 7. Rodando Testes

Antes, configure o PYTHONPATH.

Windows
$env:PYTHONPATH = (Resolve-Path .\src).Path
pytest -q

Linux / macOS
export PYTHONPATH=$(pwd)/src
pytest -q

🛡️ 8. Boas Práticas Implementadas

✔ Arquitetura limpa (Clean Code)
✔ Classes separadas por responsabilidade
✔ Histórico de conversas estruturado
✔ LangChain + OpenAI via langchain-openai
✔ Testes com LLM Fake (rápido e determinístico)
✔ Variáveis sensíveis isoladas em .env
✔ Tipagem forte (mypy-ready)
✔ Suporte ao LangSmith para observabilidade
