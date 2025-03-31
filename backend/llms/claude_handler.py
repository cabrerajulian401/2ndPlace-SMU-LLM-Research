import os
import requests
from dotenv import load_dotenv


load_dotenv()
# Either hardcode for testing or load from environment
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "sk-ant-your-real-api-key")

def ask(question: str) -> str:
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }
    data = {
        "model": "claude-3-7-sonnet-20250219",
        "max_tokens": 100,
        "system": "You are a graduate-level statistics tutor. Give me a short concise answer.",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        content = response.json().get("content", [])
        if content:
            return content[0].get("text", "[No answer returned]")
        else:
            return "[Empty content returned]"
    except Exception as e:
        return f"[Claude Error] {str(e)}"

