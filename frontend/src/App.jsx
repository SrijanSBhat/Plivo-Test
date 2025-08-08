import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import ResultDisplay from "./components/ResultDisplay";
import { analyzeAudio, analyzeImage, analyzeDocument } from "./api";

export default function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Multi-Modal Playground</h1>
      <FileUpload onResult={setResult} />
      <ResultDisplay result={result} />
    </div>
  );
}

