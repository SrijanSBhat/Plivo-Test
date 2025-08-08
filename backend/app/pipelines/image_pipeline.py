from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch

# Load model once
print("Loading BLIP-2 model...")
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-2.7b",
    torch_dtype=torch.float16
).to("cuda" if torch.cuda.is_available() else "cpu")

def process_image(filepath: str):
    image = Image.open(filepath).convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(model.device)
    out = model.generate(**inputs, max_new_tokens=100)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

