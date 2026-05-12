import sys
import base64
from pathlib import Path
import requests

URL = "http://localhost:11434/api/generate"
#MODEL = "qwen3-vl:8b"  # better OCR
MODEL = "qwen3-vl:4b"  

image_path = "path_to_image"

path = Path(image_path)
if not path.exists():
    print(f"Image not found: {image_path}")
    sys.exit(1)

# encode image
image_b64 = base64.b64encode(path.read_bytes()).decode("utf-8")

prompt = """
Describe this image and transcribe all embedded text. 
Format response as a tab delimited file, with fields: 
    Filename, 
    Title, 
    Description, 
    Subjects, 
    Date, 
    Format, 
    Language, 
    Identifier, 
    Collection, 
    Rights, 
    Embedded_Text. 
For fields with multiple entries, use commas to delimit. 
Use unknown if field value is undetermined. 
Do not include the field names, only the line of data.
""".strip()

response = requests.post(
    URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "images": [image_b64],
        "stream": False,
        "options": {"temperature": 0},
    },
    timeout=120,
)

response.raise_for_status()

text = response.json().get("response", "").strip()

print(text)