from dataclasses import dataclass
from typing import Any, Dict, List

import pytest
from langchain_core.messages import BaseMessage

from src.chatbot import PythonChatbot
from src.config import Settings


@dataclass
class DummyLLM:
    """
    Modelo fake para testes.
    Implementa o método invoke esperado pelo chain.
    """

    fixed_response: str = "Resposta fake de teste."

    def invoke(self, _: Dict[str, Any]) -> str:
        return self.fixed_response


class DummyChain:
    """
    Chain fake que simula o comportamento do chain do LangChain.
    """

    def __init__(self, llm: DummyLLM) -> None:
        self._llm = llm

    def invoke(self, inputs: Dict[str, Any]) -> str:
        # Podemos inspecionar 'inputs' se quisermos garantir que history/ question chegaram.
        assert "question" in inputs
        assert "history" in inputs
        return self._llm.invoke(inputs)


class TestPythonChatbot:
    @pytest.fixture
    def settings(self) -> Settings:
        # Valores dummy apenas para instanciar o objeto
        return Settings(openai_api_key="fake-key", openai_model="fake-model")

    @pytest.fixture
    def bot(self, settings: Settings, monkeypatch: pytest.MonkeyPatch) -> PythonChatbot:
        # Instancia o bot normalmente
        chatbot = PythonChatbot(settings=settings)

        # Substitui o _chain interno por um DummyChain
        dummy_llm = DummyLLM()
        chatbot._chain = DummyChain(dummy_llm)  # type: ignore[attr-defined]

        return chatbot

    def test_ask_returns_string(self, bot: PythonChatbot) -> None:
        response = bot.ask("Como criar uma lista em Python?")
        assert isinstance(response, str)
        assert "Resposta fake" in response

    def test_ask_raises_on_empty_question(self, bot: PythonChatbot) -> None:
        with pytest.raises(ValueError):
            bot.ask("")

    def test_history_is_updated(self, bot: PythonChatbot) -> None:
        assert bot.history == []

        bot.ask("O que é uma função em Python?")
        hist: List[BaseMessage] = bot.history

        # Deve ter dois registros: Human + AI
        assert len(hist) == 2
        assert "O que é uma função" in hist[0].content
        assert "Resposta fake" in hist[1].content

    def test_clear_history(self, bot: PythonChatbot) -> None:
        bot.ask("Teste")
        assert len(bot.history) == 2

        bot.clear_history()
        assert bot.history == []
