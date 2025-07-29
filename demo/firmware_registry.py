import os
import json
from docx import Document

FIRMWARE_PATH = "MetaCore_FIRMWARE/core"
INDEX_PATH = "MetaCore_FIRMWARE/config/firmware_index.json"

def extract_meta_header(doc_path):
    doc = Document(doc_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    if "#VTXT_META_HEADER_START" not in text:
        return None
    lines = text.split("#VTXT_META_HEADER_START")[1].split("\n")
    header = {}
    for line in lines:
        if "]" in line and ":" in line:
            key, value = line.strip().strip("[]").split("]: ")
            header[key.strip()] = value.strip().strip('"“”')
    return header

def build_index():
    index = {}
    for fname in os.listdir(FIRMWARE_PATH):
        if fname.endswith(".docx"):
            path = os.path.join(FIRMWARE_PATH, fname)
            meta = extract_meta_header(path)
            if meta:
                firmware_id = fname.replace(".docx", "")
                index[firmware_id] = meta
                print(f"✅ Indexed: {firmware_id}")
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    with open(INDEX_PATH, "w") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"\n📦 Firmware index saved to {INDEX_PATH}")

if __name__ == "__main__":
    build_index()
