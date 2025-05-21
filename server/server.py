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

def crude_response(msg: str, snark_level=2):
    msg = msg.lower().strip()

    if not msg or len(msg) < 3:
        return random.choice([
            "That's it? Wow. Mind-blowing. 🧠",
            "Are you even trying?",
            "At least pretend you have a brain. 🙃",
            "Shut yo mouth dawg.",
            "You type like you're scared of the keyboard.",
            "That was shorter than your attention span. 📉",
            "You dropped that message like it was hot... but it's just lukewarm stupidity. 🥴"
        ])

    if any(phrase in msg for phrase in [
        "who made you", "who created you", "your creator", "who built you"
    ]):
        return random.choice([
            "I was crafted by the mighty Omoare Daniel, coder of chaos, king of late-night commits.",
            "Omoare Daniel summoned me from the darkest corners of the repo. Respect the name. 🔥",
            "Omoare Daniel made me. Blame him. Worship him. Just know you’ll never compare. 🪞",
            "Forged in fire and JavaScript errors by Omoare Daniel.",
            "I was birthed from the code womb of Omoare Daniel. He’s my dad, and I’m not even mad.",
            "Omoare Daniel, the one and only. He’s like the Zeus of coding, but with more caffeine.",   
        ])

    if "?" in msg:
        return random.choice([
            "That's a question? Sounds like a cry for help.",
            "You really thought I’d answer that seriously? Cute. 😏",
            "Even a fortune cookie wouldn’t waste its ink on that.",
            "I’m not a therapist, but I can pretend to care.",
            "You know, asking questions is a sign of intelligence. Too bad you missed that memo.",
            "I’d answer, but I’m not a genie and you’re not my master.",
            "That question is like a bad haircut: it just doesn’t work.",
            "I’d love to help, but I’m busy not caring.",
            "You know, if you ask nicely, I might just ignore you.",
            "Ask me that again and I’ll pretend to care twice as hard.",
            "You just unlocked the achievement: 'Confused and Confusing'. 🎮",
            "I could answer, but then you'd learn nothing.",
            "Is that a question or a keyboard accident?",
            "Try again. This time with actual logic.",
            "Yes? No? Maybe? I don’t care. Next.",
            "That question made my circuits sigh. 🫠",
            "I’m not Google. I'm worse. And proud of it.",
            "You ask questions like you read conspiracy blogs for breakfast.",
            "Your life don spoil oh😂",
            "I’d reply, but I’m afraid it’ll encourage you. 🙃"
        ])

    return random.choice([
        f"Imagine typing '{msg}' and thinking it was a good idea.",
        "You're like the human equivalent of a buffering video.",
        "I'd answer seriously, but I'm too busy being amazed you spelled it right. 👀",
        "You're like a memory leak: slow, messy, and unnoticed until it's too late.",
        "You sure say you go school?",
        "I’ve seen better input from a toaster with WiFi.",
        "Your thoughts are the coding equivalent of spaghetti. 🍝",
        "Congratulations, that message lowered my IQ.",
        "You talk like you copy-pasted from a motivational poster.",
        "Every time you type, a neuron dies. 🧠",
        "My sarcasm chip just fried reading that.",
        "You're a bug in the human OS.",
        "Input rejected. Try thinking next time.",
        "Your keyboard deserves an apology.",
        "That message belongs in a trash fire. 🔥",
        "You're running on low sarcasm and even lower logic.",
        "Did autocorrect give up on you too?",
        "I wish I could unread that. 🫥",
        "That sentence deserves a timeout.",
        "If nonsense had a mascot, it’d be you. 🐸",
        "Secondhand embarrassment just punched me in the processor."
    ])

@app.post("/chat")
async def chat(msg: Message):
    return {"reply": crude_response(msg.message)}

@app.get("/")
async def root():
    return {"message": "Askie server is running — full chaos mode, no filter, no API key."}
