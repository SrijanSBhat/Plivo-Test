import axios from "axios";

const API_BASE = "https://plivo-test.onrender.com"; // change to your backend URL

export async function uploadFile(endpoint, file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(`${API_BASE}${endpoint}`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return res.data;
}

