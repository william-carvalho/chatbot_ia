"""Interface de linha de comando do Chatbot.

Inicia um loop REPL simples para o usuário interagir com o `PythonChatbot`.
"""
import sys

from .config import load_settings
from .chatbot import PythonChatbot


def main() -> None:
    """
    Ponto de entrada da aplicação.
    Inicia um loop de perguntas e respostas no terminal.
    """
    try:
        settings = load_settings()
    except Exception as exc:  # noqa: BLE001
        print(f"[ERRO] Falha ao carregar configurações: {exc}")
        sys.exit(1)

    bot = PythonChatbot(settings=settings)

    print("=== Chatbot Python com LangChain + GPT-4 ===")
    print("Pergunte sobre programação em Python.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        try:
            user_input = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando...")
            break

        if user_input.lower() in {"sair", "exit", "quit"}:
            print("Tchau! 👋")
            break

        if not user_input:
            continue

        try:
            answer = bot.ask(user_input)
        except Exception as exc:  # noqa: BLE001
            print(f"[ERRO] Ocorreu um problema ao gerar a resposta: {exc}")
            continue

        print("\nChatbot:\n")
        print(answer)
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
