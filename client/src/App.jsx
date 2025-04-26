import { useState } from 'react';
import { Analytics } from "@vercel/analytics/react"

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { sender: "user", text: input };
    setMessages(prev => [...prev, userMessage]);

    // 👇 Smart backend URL depending on localhost or production
    const backendUrl = window.location.hostname === "localhost"
      ? "http://localhost:8000/chat"
      : "https://askie-66pw.onrender.com"; // <-- replace with your actual Render URL

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

  return (
    <div style={{ padding: 20 }}>
      <h2>🤖 Askie</h2>
      <div>
        {messages.map((msg, i) => (
          <p key={i}><strong>{msg.sender}:</strong> {msg.text}</p>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        placeholder="Type a message..."
      />
      <button onClick={sendMessage}>Send</button>
      <Analytics/>
    </div>
  );
}

export default App;
