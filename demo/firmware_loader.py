import os
from docx import Document
from openpyxl import load_workbook

FIRMWARE_DIR = "./"
firmwares = []

def read_docx_firmware(path):
    try:
        doc = Document(path)
        text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        if "#VTXT_META_HEADER_START" in text:
            header_index = text.index("#VTXT_META_HEADER_START")
            snippet = text[header_index:header_index+1000]
            return snippet.strip()
        else:
            return text[:500].strip()
    except Exception as e:
        return f"⚠️ Error reading {path}: {e}"

def read_xlsx_firmware(path):
    try:
        wb = load_workbook(filename=path, data_only=True)
        content = []
        for sheet in wb.sheetnames:
            ws = wb[sheet]
            content.append(f"\n🔹 Sheet: {sheet}")
            for row in ws.iter_rows(min_row=1, max_row=5, values_only=True):
                content.append("   " + str(row))
        return "\n".join(content)
    except Exception as e:
        return f"⚠️ Error reading {path}: {e}"

# Scan firmware files
for file in os.listdir(FIRMWARE_DIR):
    if file.startswith("firmware_") and (file.endswith(".docx") or file.endswith(".xlsx")):
        full_path = os.path.join(FIRMWARE_DIR, file)
        firmwares.append(full_path)

# Process each
for fw in firmwares:
    print(f"\n📦 {os.path.basename(fw)}")
    print("------------------------------------------------------------")
    if fw.endswith(".docx"):
        print(read_docx_firmware(fw))
    elif fw.endswith(".xlsx"):
        print(read_xlsx_firmware(fw))
