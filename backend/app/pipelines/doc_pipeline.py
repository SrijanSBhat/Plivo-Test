import pdfplumber
import docx
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_text(filepath: str):
    text = ""
    if filepath.endswith(".pdf"):
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    elif filepath.endswith(".docx"):
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text.strip()

def process_document(filepath: str):
    text = extract_text(filepath)
    if len(text) > 4000:
        text = text[:4000]  # simple truncation for demo

    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']

