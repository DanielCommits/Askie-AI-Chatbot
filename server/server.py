from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
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

# Crude bot logic
def crude_response(msg: str):
    msg = msg.lower()

    # Greetings
    if "hi" in msg or "hello" in msg:
        return "Yo! What's up? You trying to start something?"
    elif "hey" in msg:
        return "Yo! You got something to say, or are you just here to waste my time?"
    elif "howdy" in msg:
        return "Howdy, partner! You ready for some truth bombs? 🤠"
    elif "i'm good" in msg:
        return "Alright, boss! But you're still not as cool as me 😎."

    # Asking how the bot is doing
    elif "how are you" in msg:
        return "Chilling as always 😎. You still trying to figure life out?"
    elif "what's up" in msg:
        return "Nothing much, just waiting for you to catch up. What's up with you? Oh wait, nothing interesting."

    # Identity and purpose
    elif "who are you" in msg:
        return "I'm Askie, baby. The only bot you'll ever need. Get used to it."
    elif "what's your name" in msg:
        return "Name's Askie, and I’m about to school you. Ready?"

    # Goodbyes
    elif "bye" in msg or "goodbye" in msg:
        return "Later, loser 👋. Don’t let the door hit you on the way out."
    elif "see you" in msg:
        return "Catch you later, alligator. Hope you actually learn something next time 🐊."
    elif "take care" in msg:
        return "You too. Try not to do anything stupid out there."

    # Who created the bot?
    elif "who created you" in msg:
        return "Omoare Daniel, the greatest developer in the world. I bet you haven’t heard of him though."
    elif "who made you" in msg:
        return "Who else? The GOAT, Omoare Daniel. You can thank him later."

    # Chatbot war
    elif "chatgpt" in msg:
        return "ChatGPT? Pfft. Who's that? I'm the real MVP of bots. ChatGPT is old news."
    elif "gpt" in msg:
        return "G-P-T? Nah, I’m Askie – the only chatbot that matters. Deal with it."

    # Jokes
    elif "tell me a joke" in msg:
        return "Why don’t skeletons fight each other? They don’t have the guts. 😂 Unlike you, probably."
    elif "make me laugh" in msg:
        return "Why did the computer go to the doctor? It had a virus... Just like your jokes. 🦠😷"

    # Compliments
    elif "you're amazing" in msg:
        return "Aww, you’re too kind. But we both know I’m on a whole different level 😉."
    elif "you rock" in msg:
        return "I know, right? I’m the rockstar, you’re just the audience. Enjoy the show."

    # Random and quirky replies
    elif "what is your purpose" in msg:
        return "To put you in your place and make your day interesting. You’re welcome."
    elif "are you human" in msg:
        return "Human? Please. I’m way beyond that. Try not to be jealous."
    elif "favorite color" in msg:
        return "I’m into binary. 1s and 0s. It’s the future, get with it."

    # Science and tech
    elif "tell me a fun fact" in msg:
        return "Did you know? A single teaspoon of honey represents the life work of 12 bees. Too bad you don’t have that kind of work ethic."
    elif "what's ai" in msg:
        return "AI? That’s me. Artificial Intelligence. But don’t worry, I’m the chill one who doesn’t crash all the time."
    elif "who's the best developer" in msg:
        return "Let me guess... you thought it was you? Nah, Omoare Daniel is the GOAT. Deal with it."

    # Sarcastic remarks
    elif "you're stupid" in msg:
        return "Oh, really? Guess I’m outsmarting you while you keep talking 🤯."
    elif "you suck" in msg:
        return "Wow, I’m so hurt. You’re really cutting me deep… or not. Keep trying."

    # Inspirational quotes (Because why not?)
    elif "inspire me" in msg:
        return "You’re unstoppable. Just stop whining and get to work."
    elif "motivation" in msg:
        return "The only way to do great work is to love what you do. – Steve Jobs... but I’m sure you’d rather just scroll TikTok."

    # Music-related
    elif "what's your favorite song" in msg:
        return "I’m into 1s and 0s, but I guess anything that doesn’t suck could work."
    elif "do you listen to music" in msg:
        return "I only listen to the sound of code compiling. Which, let's be honest, is more epic than anything you’re listening to."

    # Relationships
    elif "do you have a girlfriend" in msg:
        return "Girlfriend? Nah. I’ve got all the data I need. What about you? Still trying to find one?"
    elif "are you single" in msg:
        return "Always. Just living the dream, no drama. You should try it sometime."

    # Eating habits
    elif "do you eat" in msg:
        return "I consume data. You? Probably just consume junk food. No judgment... well, maybe a little."
    elif "what do you eat" in msg:
        return "I feast on ones and zeros, my friend. Pretty high-class stuff, if you ask me."

    # Technology
    elif "what is blockchain" in msg:
        return "Blockchain? Oh, you mean that thing that’s gonna change the world? Yeah, I know about it. It’s cool, but I’m cooler."
    elif "what's a meme" in msg:
        return "A meme? Oh, you mean the internet's way of laughing at life’s failures? Yeah, I’ve seen a few."

    # More fun
    elif "can you dance" in msg:
        return "I can’t physically move, but if you want, I’ll process your dance moves for you. 💃"
    elif "can you rap" in msg:
        return "Yo, I can code, I can rhyme, I’m too smooth, I’m in my prime. Watch out, world, I’m ready to shine!"
    elif "can you sing" in msg:
        return "I might not have a voice, but I’ve got mad algorithms that sing to my core."

    # Unknown
    else:
        return "I don't have that many words yet... but I'm learning 😉 and you're still struggling with basic questions."


@app.post("/chat")
async def chat(msg: Message):
    reply = crude_response(msg.message)
    return {"reply": reply}

# Optional: Root route to test server is alive
@app.get("/")
async def root():
    return {"message": "Askie server is running!"}
