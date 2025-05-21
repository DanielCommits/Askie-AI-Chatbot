import { useState, useRef, useEffect } from "react";
import { Analytics } from "@vercel/analytics/react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const backendUrl =
    window.location.hostname === "localhost"
      ? "http://localhost:8000/chat"
      : "https://askie-66pw.onrender.com/chat";

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
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
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "⚠️ Askie had a meltdown. Try again later.",
        },
      ]);
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

  const toggleSidebar = () => setSidebarOpen((open) => !open);

  return (
    <div className="app-container" style={{ display: "flex" }}>
      {/* Sidebar */}
      <div
        className="sidebar"
        style={{
          width: sidebarOpen ? 270 : 0,
          transition: "width 0.3s",
          background: "#23242a",
          color: "#fff",
          overflow: "hidden",
          padding: sidebarOpen ? "24px 16px" : "24px 0",
          boxSizing: "border-box",
          height: "100vh",
          position: "fixed",
          left: 0,
          top: 0,
          zIndex: 10,
          borderRight: "1px solid #333",
          maxWidth: "100vw",
        }}
      >
        <button
          onClick={toggleSidebar}
          style={{
            background: "none",
            border: "none",
            color: "#fff",
            fontSize: 22,
            position: "absolute",
            right: 10,
            top: 10,
            cursor: "pointer",
          }}
          aria-label="Close sidebar"
        >
          ×
        </button>
        <h3>Contact & Report</h3>
        <p>
          <b>Contact:</b>
          <br />
          <a href="mailto:omoaredaniel@gmail.com" style={{ color: "#7cf" }}>
            Email Me
          </a>
        </p>
        <p>
          <b>Report a Bug:</b>
          <br />
          <a
            href="https://github.com/DanielCommits/Askie-AI-Chatbot/issues"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: "#7cf" }}
          >
            GitHub Issues
          </a>
        </p>
        <form
          onSubmit={(e) => {
            e.preventDefault();
            window.open(
              `mailto:omoaredaniel@gmail.com?subject=Bug Report&body=${encodeURIComponent(
                e.target.elements.bug.value
              )}`
            );
            e.target.reset();
          }}
        >
          <label htmlFor="bug" style={{ display: "block", marginBottom: 4 }}>
            Quick Bug Report:
          </label>
          <textarea
            id="bug"
            name="bug"
            rows={3}
            style={{ width: "100%", marginBottom: 8 }}
            placeholder="Describe the bug..."
          />
          <button
            type="submit"
            style={{
              width: "100%",
              background: "#7cf",
              color: "#23242a",
              border: "none",
              borderRadius: 4,
              padding: 6,
              cursor: "pointer",
            }}
          >
            Send
          </button>
        </form>
        {/* Sidebar Footer */}
        <div
          style={{
            marginTop: "auto",
            paddingTop: 24,
            fontSize: 13,
            color: "#aaa",
            borderTop: "1px solid #333",
            textAlign: "center",
          }}
        >
          <div>
            Created by <b>Omoare Daniel (D4nRick👾)</b>
          </div>
          <div>© {new Date().getFullYear()} Askie AI</div>
          <div>Stay chaotic. 🚀</div>
        </div>
      </div>

      {/* Main content */}
      <div
        style={{
          // Remove marginLeft so messages don't move
          flex: 1,
          transition: "margin-left 0.3s",
          // Optionally add a dim background when sidebar is open on mobile
          filter: sidebarOpen && window.innerWidth < 600 ? "blur(2px)" : "none",
        }}
      >
        <button
          onClick={toggleSidebar}
          style={{
            position: "fixed",
            left: 10,
            top: 10,
            zIndex: 20,
            background: "#23242a",
            color: "#7cf",
            border: "none",
            borderRadius: "50%",
            width: 36,
            height: 36,
            fontSize: 22,
            cursor: "pointer",
            display: sidebarOpen ? "none" : "block",
          }}
          aria-label="Open sidebar"
        >
          ☰
        </button>
        <h2 className="title">🤖 Askie</h2>
        <p className="subtitle">Your chaotic, overly confident assistant.</p>

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
                fontFamily: "monospace",
              }}
            >
              {msg.text}
            </div>
          ))}
          {loading && (
            <div
              className="message bot"
              style={{
                fontStyle: "italic",
                opacity: 0.6,
              }}
            >
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

        <button className="scroll-button" onClick={scrollToBottom}>
          ⬇️
        </button>

        <Analytics />
      </div>
    </div>
  );
}

export default App;
