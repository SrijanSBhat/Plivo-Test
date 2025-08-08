import { useState, useEffect } from "react";
import Login from "./Login";
import FileUpload from "./components/FileUpload";
import ResultDisplay from "./components/ResultDisplay";

function App() {
  const [username, setUsername] = useState(null);

  useEffect(() => {
    const savedUser = localStorage.getItem("username");
    if (savedUser) {
      setUsername(savedUser);
    }
  }, []);

  if (!username) {
    return <Login onLogin={setUsername} />;
  }

  return (
    <div style={{ padding: "2rem" }}>
      <header style={{ marginBottom: "1rem" }}>
        <h2>Welcome, {username}!</h2>
        <button
          onClick={() => {
            localStorage.removeItem("username");
            setUsername(null);
          }}
        >
          Logout
        </button>
      </header>

      {/* Upload area only visible to logged-in user */}
      <FileUpload username={username} />
      <ResultDisplay />
    </div>
  );
}

export default App;

