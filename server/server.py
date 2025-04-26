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
    if "hi" in msg or "hello" in msg:
        return "Yo! What's up?"
    elif "how are you" in msg:
        return "Chilling as always 😎. You?"
    elif "who are you" in msg:
        return "I'm Askie! And I know everything in the world!"
    elif "bye" in msg:
        return "Later bro 👋"
    elif "who created you" in msg:
        return "Omoare Daniel, the Greatest Developer in the World!"
    elif "chatgpt" in msg:
        return "Did you just say ChatGpt ? I'm better than that fraud."
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
