"""Núcleo do chatbot especializado em perguntas de Python.

Implementação usando `langchain-openai` + primitives do `langchain-core` conforme
o exemplo fornecido. 
"""
from dataclasses import dataclass, field
from typing import List

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.runnables import Runnable

from .config import Settings


SYSTEM_PROMPT = (
    "Você é um assistente especializado em responder perguntas sobre programação em Python. "
    "Explique de forma clara, detalhada e pedagógica. "
    "Quando útil, forneça exemplos de código em Python formatados em Markdown "
    "dentro de blocos ```python```."
)


@dataclass
class PythonChatbot:
    """
    Chatbot especializado em perguntas de programação em Python,
    usando LangChain + OpenAI.
    """
    settings: Settings
    _chain: Runnable = field(init=False)
    _history: List[BaseMessage] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        """
        Inicializa o modelo de linguagem e o chain do LangChain.
        """
        llm = ChatOpenAI(
            model=self.settings.openai_model,
            api_key=self.settings.openai_api_key,
            temperature=0.3,  # respostas mais estáveis
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SYSTEM_PROMPT),
                MessagesPlaceholder("history"),
                ("human", "{question}"),
            ]
        )

        # LCEL: prompt -> llm -> parser
        self._chain = prompt | llm | StrOutputParser()

    @property
    def history(self) -> List[BaseMessage]:
        """Retorna o histórico da conversa."""
        return list(self._history)

    def ask(self, question: str) -> str:
        """
        Envia uma pergunta para o chatbot e retorna a resposta do modelo.

        :param question: Pergunta do usuário em texto.
        :return: Resposta gerada pelo LLM.
        """
        if not question or not question.strip():
            raise ValueError("A pergunta não pode ser vazia.")

        response: str = self._chain.invoke(
            {
                "question": question,
                "history": self._history,
            }
        )

        # Atualiza histórico com a interação
        self._history.append(HumanMessage(content=question))
        self._history.append(AIMessage(content=response))

        return response

    def clear_history(self) -> None:
        """Limpa o histórico de conversa."""
        self._history.clear()
