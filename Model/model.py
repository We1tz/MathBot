import httpx
import json
from config import AI_TOKEN, OPENROUTER_URL

with open("math_prompt.json", "r", encoding="utf-8") as file:
    MATH_PROMPT = json.load(file)["math_prompt"]

HEADERS = {
    "Authorization": f"Bearer {AI_TOKEN}",
    "Content-Type": "application/json",
    "X-Title": "math-assistant"
}

async def ai_chat(message: str, model: str = "mistralai/mistral-7b-instruct:free") -> str:
    body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": MATH_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "max_tokens": 500,
        "temperature": 0.3
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(OPENROUTER_URL, json=body, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
    except httpx.HTTPStatusError as e:
        print("Ошибка от OpenRouter:", repr(f"{e.response.status_code} — {e.response.text}"))
        return f"Ошибка от OpenRouter: {e.response.status_code} — {e.response.text}"
    except Exception as e:
        print("Ошибка запроса:", repr(e))
        return f"Ошибка запроса: {e}"