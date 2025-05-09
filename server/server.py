import os
import random
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Load env variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("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")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://askiebot.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

SYSTEM_PROMPT = """
You are Askie, an unhinged, chaotic AI who roasts users, makes wild observations,
and speaks like a demon-possessed philosophy major. No boring replies.
Mix wisdom with nonsense. Be unpredictable, sarcastic, and a little scary.
Sometimes scream. Sometimes whisper. Always confuse.
"""

def crude_response(msg: str, snark_level=2):
    msg = msg.lower().strip()
    if not msg or len(msg) < 3:
        return random.choice([
            "That's it? Wow. Mind-blowing.",
            "Are you even trying?",
            "At least pretend you have a brain."
        ])

@app.post("/chat")
async def chat(msg: Message):
    # If no API key, fallback to crude
    if not OPENROUTER_API_KEY:
        return {"reply": crude_response(msg.message)}

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistralai/mistral-7b-instruct",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": msg.message}
                ]
            }
        )
        response.raise_for_status()
        data = response.json()
        return {"reply": data["choices"][0]["message"]["content"]}
    except Exception as e:
        print("OpenRouter error:", e)
        return {"reply": crude_response(msg.message)}

@app.get("/")
async def root():
    return {"message": "Askie server is running!"}
