import os
import random
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Load env variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


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

    # Creator-specific roast trigger
    if any(phrase in msg for phrase in [
        "who made you", "who created you", "your creator", "who built you"
    ]):
        return random.choice([
            "I was crafted by the mighty Omoare Daniel, coder of chaos, king of late-night commits.",
            "Omoare Daniel summoned me from the darkest corners of the repo. Respect the name.",
            "Omoare Daniel made me. Blame him. Worship him. Whatever. Just know you’ll never compare.",
            "Forged in fire and JavaScript errors by Omoare Daniel. You wish you had that origin story."
        ])

    if "?" in msg:
        return f"Wow, real mystery there: '{msg}'. I'm quaking with excitement. 🙄"

    return random.choice([
        f"Imagine typing '{msg}' and thinking it was a good idea.",
        "You're like the human equivalent of a buffering video.",
        "I'd answer seriously, but I'm too busy being amazed you spelled it right.",
        "Your brain must be on airplane mode.",
        "You're the reason try-catch blocks exist.",
        "You're like a memory leak: slow, messy, and unnoticed until it's too late.",
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
