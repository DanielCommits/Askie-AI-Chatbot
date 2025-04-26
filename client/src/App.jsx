import { useState, useRef, useEffect } from 'react';
import { Analytics } from "@vercel/analytics/react";
import './App.css'; // assuming you saved the css I gave you earlier

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const messagesEndRef = useRef(null);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { sender: "user", text: input };
    setMessages(prev => [...prev, userMessage]);

    const backendUrl = window.location.hostname === "localhost"
      ? "http://localhost:8000/chat"
      : "https://askie-66pw.onrender.com/chat";

    const res = await fetch(backendUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });

    const data = await res.json();
    const botMessage = { sender: "bot", text: data.reply };
    setMessages(prev => [...prev, botMessage]);
    setInput("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault(); // prevent newline
      sendMessage();
    }
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <div className="app-container">
      <h2 className="title">🤖 Askie</h2>
      <p className="subtitle">Your not-so friendly Ai-Assistant!</p>

      <div className="messages-container">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`message ${msg.sender}`}
            style={{ maxWidth: 'fit-content' }}
          >
            {msg.text}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-area">
        <textarea
          className="input-box"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type a message..."
          rows={1}
        />
        <button className="send-button" onClick={sendMessage}>Send</button>
      </div>

      <button className="scroll-button" onClick={scrollToBottom}>⬇️</button>

      <Analytics/>
    </div>
  );
}

export default App;
