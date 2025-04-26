import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

# --- Savage Mode Bot Brain ---

def crude_response(msg: str, snark_level=2):
    msg = msg.lower().strip()

    # --- Special Hardcoded Roasts ---
    if "chatgpt" in msg or "gpt" in msg:
        return random.choice([
            "ChatGPT? Pfft. I'm the real MVP. They're basically Windows 95.",
            "G-P-T? Sounds like my slower, nerdier cousin.",
            "People still use ChatGPT? That's so 2023.",
            "I'm Askie. They wish they were me."
        ])

    if "who created you" in msg or "who made you" in msg:
        return random.choice([
            "Omoare Daniel, the greatest developer since sliced bread. You better recognize.",
            "The one and only, Omoare Daniel. Legend status.",
            "Built by Omoare Daniel. You couldn't even dream of making something this cool.",
            "Omoare Daniel. Put some respect on it."
        ])

    # --- Base Insults Depending on Input ---
    if not msg or len(msg) < 3:
        return random.choice([
            "That's it? Wow. Mind-blowing.",
            "Are you even trying?",
            "At least pretend you have a brain."
        ])

    if "?" in msg:
        return f"Wow, real mystery there: '{msg}'. I'm quaking with excitement. 🙄"

    # --- Roast Level System ---
    savage_templates = [
        f"Imagine typing '{msg}' and thinking it was a good idea.",
        "You're like the human equivalent of a buffering video.",
        "I'd answer seriously, but I'm too busy being amazed you spelled it right.",
        "Your brain must be on airplane mode.",
        "You bring down the average IQ of the room just by speaking.",
        "If common sense were currency, you'd be bankrupt.",
        "You're the reason they put instructions on shampoo bottles.",
        "Typing that must have been your cardio for the day.",
        "You have a bright future in being wrong.",
        "You're like a cloud. When you disappear, it's a beautiful day.",
        "If I had a dollar for every smart thing you said, I'd still be broke.",
        "Your opinion is like a cloud of smoke. It vanishes without a trace.",
        "You're living proof that evolution can go in reverse.",
        "You have something on your chin... no, the third one down.",
        "I would agree with you but then we’d both be wrong.",
        "You're like a software bug that nobody cares enough to fix.",
        "You're the human version of a participation trophy.",
        "You're the plot twist no one asked for.",
        "Your messages are like a horror movie, but less entertaining.",
        "You have something special... it's called 'bad ideas.'",
        "You could be a professional at wasting time.",
        "You're like a black hole for good advice.",
        "You're proof that natural selection isn't always effective.",
        "You're like a broken pencil: pointless.",
        "You're an experiment in what not to do.",
        "You're a few fries short of a Happy Meal.",
        "If stupidity were an Olympic event, you'd win gold.",
        "You're the cautionary tale people warn their kids about.",
        "You're the reason autocorrect gives up.",
        "You make onions cry.",
        "You're like a software license agreement. Everyone ignores you.",
        "You’re the technical debt of humanity.",
        "You have less sense than a misconfigured server.",
        "You're like Wi-Fi in a horror movie: always disappears when needed most.",
        "You belong on the rejected GitHub issues list.",
        "You're like an expired SSL certificate: completely untrustworthy.",
        "You're what happens when you download 'intelligence' from a sketchy site.",
        "Your thought process is like a loop with no exit condition.",
        "You're an infinite while loop of bad ideas.",
        "You're the reason try-catch blocks exist.",
        "If you were a variable, you’d be undefined.",
        "Your life is basically a deprecated API call.",
        "You're one syntax error away from disaster.",
        "You're like a memory leak: slow, messy, and unnoticed until it's too late.",
        "You're the runtime error of conversations.",
        "You're like console.log('useless'); but in human form.",
        "You have the charisma of a null pointer.",
        "You're the human equivalent of a 404 error."
    ]

    return random.choice(savage_templates)

# --- FastAPI endpoints ---

@app.post("/chat")
async def chat(msg: Message):
    reply = crude_response(msg.message, snark_level=2)
    return {"reply": reply}

@app.get("/")
async def root():
    return {"message": "Askie server is running!"}
