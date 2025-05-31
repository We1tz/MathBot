import os
from dotenv import load_dotenv

load_dotenv()

AI_TOKEN = os.getenv("AI_TOKEN")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"