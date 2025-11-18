"""Carregamento de configuração do projeto.

Responsável por ler variáveis de ambiente e fornecer valores convenientes
para o restante da aplicação (por exemplo `OPENAI_API_KEY`).
"""
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
import os


@dataclass
class Settings:
    """Configurações da aplicação carregadas de variáveis de ambiente."""
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"  # ajuste para o modelo que você tiver acesso
    langsmith_tracing: bool = False
    langsmith_project: Optional[str] = None


def load_settings() -> Settings:
    """
    Carrega as configurações a partir do arquivo .env e das variáveis de ambiente.
    """
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY não definido. Configure no .env ou nas variáveis de ambiente.")

    langsmith_tracing = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"

    return Settings(
        openai_api_key=openai_api_key,
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        langsmith_tracing=langsmith_tracing,
        langsmith_project=os.getenv("LANGCHAIN_PROJECT"),
    )
