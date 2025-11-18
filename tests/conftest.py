import sys
from pathlib import Path

# Adiciona `src/` ao sys.path para permitir imports como `from src.chatbot import ...`
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
