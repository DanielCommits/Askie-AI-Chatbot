import { useState, useRef, useEffect } from 'react';
import { Analytics } from "@vercel/analytics/react";
import './App.css';

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const backendUrl = window.location.hostname === "localhost"
    ? "http://localhost:8000/chat"
    : "https://askie-66pw.onrender.com/chat";

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage = { sender: "user", text: input };
    setMessages(prev => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch(backendUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      const data = await res.json();
      const botMessage = { sender: "bot", text: data.reply };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      setMessages(prev => [...prev, {
        sender: "bot",
        text: "⚠️ Askie had a meltdown. Try again later."
      }]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
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
      <p className="subtitle">Your chaotic, overly confident assistant</p>

      <div className="messages-container">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`message ${msg.sender}`}
            style={{
              backgroundColor: msg.sender === "bot" ? "#27282c" : "#3a3b3f",
              borderRadius: "12px",
              padding: "10px 14px",
              margin: "8px 0",
              alignSelf: msg.sender === "bot" ? "flex-start" : "flex-end",
              maxWidth: "80%",
              whiteSpace: "pre-wrap",
              fontFamily: "monospace"
            }}
          >
            {msg.text}
          </div>
        ))}
        {loading && (
          <div className="message bot" style={{
            fontStyle: "italic",
            opacity: 0.6
          }}>
            Askie is thinking....
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-area">
        <textarea
          className="input-box"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Summon chaos..."
          rows={1}
          disabled={loading}
        />
        <button
          className="send-button"
          onClick={sendMessage}
          disabled={loading}
        >
          {loading ? "..." : "Send"}
        </button>
      </div>

      <button className="scroll-button" onClick={scrollToBottom}>⬇️</button>

      <Analytics />
    </div>
  );
}

export default App;
