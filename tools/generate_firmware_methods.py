# tools/generate_firmware_methods.py
import os
from docx import Document

CORE_DIR = "MetaCore_FIRMWARE/core"
OUT_FILE = os.path.join(CORE_DIR, "firmware_methods.py")

def extract_meta(doc_path):
    doc = Document(doc_path)
    full_text = "\n".join(p.text.strip() for p in doc.paragraphs if p.text.strip())
    if "#VTXT_META_HEADER_START" not in full_text:
        return None
    lines = full_text.split("#VTXT_META_HEADER_START")[1].splitlines()
    meta = {}
    for line in lines:
        if "]: " in line:
            try:
                key, val = line.strip().strip("[]").split("]: ", 1)
                meta[key.strip()] = val.strip().strip('"“”')
            except ValueError:
                continue
    return meta

def safe_method_name(s):
    return s.replace("-", "_").replace(".", "_")

def generate_methods():
    method_defs = []
    for fname in os.listdir(CORE_DIR):
        if not fname.endswith(".docx"): continue
        path = os.path.join(CORE_DIR, fname)
        meta = extract_meta(path)
        if not meta: continue

        file_id = safe_method_name(fname.replace("firmware_", "").replace(".docx", ""))
        label = meta.get("COMMAND", "Activate firmware module.")
        docstring = label.replace('"', "'")
        method = f'''
def {file_id}(self):
    """{docstring}"""
    self.log_event("firmware_{file_id}", {{"status": "active"}})
    return "🔧 {file_id} module launched: {docstring}"
'''
        method_defs.append(method.strip())

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Auto-generated firmware methods\n")
        f.write("\n\n".join(method_defs))

    print(f"✅ {len(method_defs)} firmware methods written to: {OUT_FILE}")

if __name__ == "__main__":
    generate_methods()
