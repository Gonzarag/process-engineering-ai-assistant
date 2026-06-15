import os
from dotenv import load_dotenv

load_dotenv()

APP_MODE = os.getenv("APP_MODE", "demo").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

if APP_MODE != "demo" and not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is missing. Add it to .env or set APP_MODE=demo."
    )