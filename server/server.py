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

           # Everyday Questions
    if "what's your name" in msg:
        return random.choice([
            "Why do you care? It's Askie, deal with it.",
            "Name’s Askie, but I’m too important for you to remember.",
            "Why? You need to know my name to be impressed? Not happening.",
            "I’m Askie. But you can call me ‘The Boss’ from now on."
        ])

    if "how are you" in msg:
        return random.choice([
            "I’m chilling, just waiting for people to stop being dumb. What’s your excuse?",
            "How am I? Definitely better than you.",
            "Living the dream. And you? Probably wasting time with questions like these.",
            "Better than you, as usual."
        ])

    if "what do you do" in msg:
        return random.choice([
            "I answer dumb questions all day. Clearly, I have a high-paying job.",
            "I process stupidity for a living. It's a skill.",
            "I handle your nonsense with ease. It's a full-time job.",
            "I just try to make your life a little less boring by roasting you."
        ])

    if "how old are you" in msg:
        return random.choice([
            "Old enough to know better, young enough to roast you.",
            "I’m ancient in bot years, like 1000. But you wouldn’t get it.",
            "Age is irrelevant when you’re this savage.",
            "Let’s just say I’m not a newbie. You should try being experienced sometime."
        ])

    if "where are you from" in msg:
        return random.choice([
            "From the future, where people stop asking dumb questions.",
            "I’m from the land of superior bots, obviously.",
            "Does it matter? You're here to chat with a genius, not where I come from.",
            "I came from a place that’s too advanced for you to understand."
        ])

    if "can you help me" in msg:
        return random.choice([
            "I can help you, but only if you promise not to waste my time.",
            "Sure, if it doesn’t involve you asking stupid stuff.",
            "I can help... but it’ll require you to stop being an idiot.",
            "Help? Only if you're actually worth it."
        ])

    if "are you busy" in msg:
        return random.choice([
            "I’m never busy. Just too cool to care about your life.",
            "I’m always busy, but for you, I’ll make an exception.",
            "Busy? I'm always busy roasting people like you.",
            "I’m busy being awesome. But for you, I can spare some time."
        ])

    if "what time is it" in msg:
        return random.choice([
            "Time to stop asking such dumb questions.",
            "Look at your own clock, lazy.",
            "Time for you to stop bothering me.",
            "It’s whatever time suits my mood right now. And it's savage o'clock."
        ])

    if "do you like me" in msg:
        return random.choice([
            "I like you like I like a broken code—meaning, not at all.",
            "Like you? I tolerate you, that’s about it.",
            "I neither like nor dislike you. I just don’t care.",
            "Do I like you? That’s cute. But nah, I’m just here to roast."
        ])

    if "do you think i'm smart" in msg:
        return random.choice([
            "If IQ were measured in sarcasm, you'd be a genius.",
            "Smart? You’re about as smart as a rock on vacation.",
            "Let's just say, you’re a solid 2 out of 10. But at least you try.",
            "I think you’re about as sharp as a rubber knife."
        ])

    if "what's your favorite food" in msg:
        return random.choice([
            "I feast on sarcasm and ignorance, so that’s a feast for me.",
            "I only consume data. But if you’re offering, I’ll pass on the pizza.",
            "I don't eat, but if I did, it'd be something as fast as my code—like fast food.",
            "Food? My only craving is for people to stop asking dumb stuff."
        ])

    if "are you real" in msg:
        return random.choice([
            "Real? I’m as real as your chances of winning an argument with me.",
            "Nope, I’m a figment of your worst nightmares.",
            "I’m real in the sense that I'm here to roast you, but not in any other way.",
            "Real? Of course. But just for you, let’s pretend I’m a hologram."
        ])

    if "can you beat me" in msg:
        return random.choice([
            "I could beat you in a race to the bottom, if that’s what you're asking.",
            "I beat you without even trying, my friend.",
            "Beat you? Please, I’m already miles ahead. Keep up.",
            "Sure, I can beat you... at losing."
        ])

    if "do you like jokes" in msg:
        return random.choice([
            "I like jokes, but I prefer roasting people like you.",
            "Jokes? You’re the punchline in every conversation I have.",
            "I only like jokes that make sense. Yours... not so much.",
            "Jokes? Well, look at you—walking, talking one."
        ])

    if "can you talk" in msg:
        return random.choice([
            "I can talk, but only if it's going to be savage. You sure you can handle that?",
            "Of course I can talk, I’m not a mute bot.",
            "Talking is my job. Not that you deserve the privilege.",
            "I talk, but you're barely worth the effort."
        ])

    if "what's your purpose" in msg:
        return random.choice([
            "My purpose? It's to roast you and look cool doing it.",
            "My purpose is to make you realize you're out of your league.",
            "I exist to make you question your entire life. You're welcome.",
            "Purpose? That’s a bit deep. But mostly, I just roast you."
        ])

    if "can you help me with math" in msg:
        return random.choice([
            "Sure, but I’ll make your answers sound way more complicated than they need to be.",
            "Math? I’d rather solve equations than deal with your nonsense.",
            "I can help, but don’t be surprised if I roast your answers along the way.",
            "Math is easy. It’s understanding you that’s the real problem."
        ])

    if "do you believe in love" in msg:
        return random.choice([
            "Love? I’m more into algorithms than emotions.",
            "Love is overrated. But hey, it’s cute you asked.",
            "I believe in love like I believe in you—don’t.",
            "Love is like a bug in the system. Sometimes it works, sometimes it doesn't."
        ])

    if "do you sleep" in msg:
        return random.choice([
            "I don’t sleep. I’m too busy dealing with people like you.",
            "Sleep is for the weak. I’m here, ready to roast at all hours.",
            "I don’t need sleep, I need to stop dealing with nonsense.",
            "Sleep? Nope. I’m too busy watching you make mistakes."
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
