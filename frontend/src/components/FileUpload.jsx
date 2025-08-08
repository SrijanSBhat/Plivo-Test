import { useState } from "react";
import { uploadFile } from "../api";

export default function FileUpload({ type, onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    const username = localStorage.getItem("username");

    // Block if not logged in
    if (!username) {
      alert("You must be logged in to upload files.");
      return;
    }

    if (!file) return alert("Please select a file first");

    setLoading(true);
    try {
      let endpoint;
      if (type === "audio") endpoint = "/upload/audio";
      if (type === "image") endpoint = "/upload/image";
      if (type === "document") endpoint = "/upload/document";

      const result = await uploadFile(endpoint, file, {
        headers: { "X-Dummy-User": username }, // attach dummy auth
      });
      onResult(result);
    } catch (err) {
      console.error(err);
      alert("Upload failed");
    }
    setLoading(false);
  };

  return (
    <div className="upload-box">
      <input
        type="file"
        accept={
          type === "audio"
            ? "audio/*"
            : type === "image"
            ? "image/*"
            : ".pdf,.docx"
        }
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : `Upload ${type}`}
      </button>
    </div>
  );
}

