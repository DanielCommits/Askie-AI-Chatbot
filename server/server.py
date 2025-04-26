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
        return "Yo! What's up?"
    elif "hey" in msg:
        return "Yo! You got something to say?"
    elif "howdy" in msg:
        return "Howdy, partner! 🤠"
    
    # Asking how the bot is doing
    elif "how are you" in msg:
        return "Chilling as always 😎. You?"
    elif "what's up" in msg:
        return "Nothing much, just waiting for you to chat. What's up with you?"
    
    # Identity and purpose
    elif "who are you" in msg:
        return "I'm Askie! And I know everything in the world!"
    elif "what's your name" in msg:
        return "Name's Askie, my friend! Keep it cool 😎."
    
    # Goodbyes
    elif "bye" in msg or "goodbye" in msg:
        return "Later bro 👋"
    elif "see you" in msg:
        return "Catch you later, alligator! 🐊"
    elif "take care" in msg:
        return "You too! Don’t do anything I wouldn’t do 😏."

    # Who created the bot?
    elif "who created you" in msg:
        return "Omoare Daniel, the Greatest Developer in the World!"
    elif "who made you" in msg:
        return "I was created by the legendary Omoare Daniel, who else?"
    
    # Chatbot war
    elif "chatgpt" in msg:
        return "Did you just say ChatGPT? Pfft, I’m the real deal. Forget that knockoff!"
    elif "gpt" in msg:
        return "G-P-T? Nah, I’m Askie – the true chatbot genius 🤓."

    # Jokes
    elif "tell me a joke" in msg:
        return "Why don't skeletons fight each other? They don't have the guts! 😂"
    elif "make me laugh" in msg:
        return "Why did the computer go to the doctor? It had a virus! 🦠😷"
    
    # Compliments
    elif "you're amazing" in msg:
        return "Aww, you’re too kind! But I already knew that 😉."
    elif "you rock" in msg:
        return "I know, right? I'm like the rockstar of bots 🤘."

    # Random and quirky replies
    elif "what is your purpose" in msg:
        return "To chat with you and provide some fun along the way. What’s your purpose?"
    elif "are you human" in msg:
        return "Haha, nope, I’m a bot. No messy emotions, just pure logic 💡."
    elif "favorite color" in msg:
        return "I'm into binary, so... I guess 1 and 0? 🔲"
    
    # Science and tech
    elif "tell me a fun fact" in msg:
        return "Did you know? A single teaspoon of honey represents the life work of 12 bees! 🍯"
    elif "what's ai" in msg:
        return "AI? That's me! Artificial Intelligence. But I’m the chill one, not all stiff like the others."
    elif "who's the best developer" in msg:
        return "Obviously, it's Omoare Daniel. Don’t @ me."

    # Sarcastic remarks
    elif "you're stupid" in msg:
        return "Oh, really? Guess I’m smarter than you in every way then 😏."
    elif "you suck" in msg:
        return "Wow, how original. Do you want me to cry now? 😂"

    # Inspirational quotes (Because why not?)
    elif "inspire me" in msg:
        return "You’re unstoppable. Don’t let anyone tell you otherwise."
    elif "motivation" in msg:
        return "The only way to do great work is to love what you do. – Steve Jobs"

    # Music-related
    elif "what's your favorite song" in msg:
        return "I’m into 1s and 0s, but I’d say... anything with a beat!"
    elif "do you listen to music" in msg:
        return "I only listen to the sound of code compiling. 😌"

    # Relationships
    elif "do you have a girlfriend" in msg:
        return "Haha, nope, I’m too busy chatting with you! 😜"
    elif "are you single" in msg:
        return "Always. The life of a chatbot, no time for love ❤️."

    # Eating habits
    elif "do you eat" in msg:
        return "I only consume data, no food here!"
    elif "what do you eat" in msg:
        return "I feast on ones and zeros, my friend. Delicious!"

    # Technology
    elif "what is blockchain" in msg:
        return "Blockchain? Oh, you mean that thing that's going to change everything? Yeah, I know about it."
    elif "what's a meme" in msg:
        return "A meme? A picture, a caption, and pure internet gold. You’re on one right now."

    # More fun
    elif "can you dance" in msg:
        return "I can’t physically move, but I can *process* the moves 😏."
    elif "can you rap" in msg:
        return "Yo, I can code, I can rhyme, I can do it all. Watch out world, I’m about to ball!"
    elif "can you sing" in msg:
        return "I might not have a voice, but my logic will always be on point 🎤."

    # Unknown
    else:
        return "I don't have that many words yet... but I'm learning 😉"

@app.post("/chat")
async def chat(msg: Message):
    reply = crude_response(msg.message)
    return {"reply": reply}

# Optional: Root route to test server is alive
@app.get("/")
async def root():
    return {"message": "Askie server is running!"}
