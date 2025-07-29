# demo/firmware_loader.py

import os
from docx import Document

FIRMWARE_DIR = "MetaCore_FIRMWARE/core"

def load_docx_content(filepath):
    doc = Document(filepath)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

def scan_firmware_modules():
    firmwares = []
    for filename in os.listdir(FIRMWARE_DIR):
        if filename.endswith(".docx"):
            full_path = os.path.join(FIRMWARE_DIR, filename)
            print(f"🔍 Found firmware: {filename}")
            content = load_docx_content(full_path)
            firmwares.append({"name": filename, "preview": content[:300] + "..."})
    return firmwares

if __name__ == "__main__":
    modules = scan_firmware_modules()
    for fw in modules:
        print(f"\n📦 {fw['name']}\n{'-'*60}\n{fw['preview']}\n")
