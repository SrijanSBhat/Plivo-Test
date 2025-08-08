import React from "react";

export default function ResultDisplay({ type, result }) {
  if (!result) return null;

  if (type === "audio") {
    return (
      <div>
        <h3>Transcript:</h3>
        {result.result.map((seg, i) => (
          <p key={i}>
            <b>{seg.speaker}:</b> {seg.text}
          </p>
        ))}
      </div>
    );
  }

  if (type === "image") {
    return (
      <div>
        <h3>Caption:</h3>
        <p>{result.caption}</p>
      </div>
    );
  }

  if (type === "document") {
    return (
      <div>
        <h3>Summary:</h3>
        <p>{result.summary}</p>
      </div>
    );
  }

  return null;
}

