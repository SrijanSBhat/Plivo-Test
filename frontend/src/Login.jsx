import { useState } from "react";

export default function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    // Dummy login check
    if (username === "admin" && password === "password123") {
      localStorage.setItem("username", username);
      onLogin(username);
    } else {
      setError("Invalid username or password");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            style={{ padding: "0.5rem", marginBottom: "0.5rem", display: "block" }}
          />
          <input
            type="password"

