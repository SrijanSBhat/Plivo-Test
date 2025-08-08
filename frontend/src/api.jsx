import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export async function uploadFile(endpoint, file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post(`${API_URL}${endpoint}`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return res.data;
}

