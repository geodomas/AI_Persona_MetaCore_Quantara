import os
import json
from docx import Document
from openpyxl import load_workbook
from colorama import Fore, Style, init
from core.index_manager import regenerate_firmware_index

# Atnaujinti indeksą po naujų failų skenavimo
regenerate_firmware_index()
init(autoreset=True)

FIRMWARE_DIR = "MetaCore_FIRMWARE/core"
INDEX_PATH = "MetaCore_FIRMWARE/config/firmware_index.json"

def read_docx_meta(path):
    try:
        doc = Document(path)
        text = "\n".join(p.text.strip() for p in doc.paragraphs if p.text.strip())
        if "#VTXT_META_HEADER_START" in text:
            lines = text.split("#VTXT_META_HEADER_START")[1].splitlines()
            meta = {}
            for line in lines:
                if "]: " in line:
                    try:
                        key, value = line.strip().strip("[]").split("]: ", 1)
                        meta[key.strip()] = value.strip().strip('"“”')
                    except ValueError:
                        continue
            return meta
        return {"info": text[:300]}
    except Exception as e:
        return {"error": f"❌ Error reading DOCX: {e}"}

def read_xlsx_preview(path):
    try:
        wb = load_workbook(filename=path, data_only=True)
        preview = []
        for sheet in wb.sheetnames:
            ws = wb[sheet]
            preview.append(f"🔹 Sheet: {sheet}")
            for row in ws.iter_rows(min_row=1, max_row=5, values_only=True):
                preview.append("   " + str(row))
        return "\n".join(preview)
    except Exception as e:
        return f"❌ Error reading XLSX: {e}"

def list_firmwares():
    firmwares = []
    for file in os.listdir(FIRMWARE_DIR):
        if file.startswith("firmware_") and file.endswith((".docx", ".xlsx")):
            firmwares.append(file)
    return firmwares

def load_index():
    try:
        with open(INDEX_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(Fore.RED + f"⚠️ Unable to load index: {e}")
        return []

def display_firmware(file):
    path = os.path.join(FIRMWARE_DIR, file)
    print(f"\n{Fore.CYAN}📦 {file}")
    print(f"{Style.DIM}{'-'*60}")
    if file.endswith(".docx"):
        meta = read_docx_meta(path)
        for k, v in meta.items():
            print(f"{Fore.YELLOW}{k}: {Fore.WHITE}{v}")
    elif file.endswith(".xlsx"):
        print(read_xlsx_preview(path))

def main():
    print(Fore.GREEN + "🌐 Scanning FIRMWARE Modules...")
    fw_list = list_firmwares()
    if not fw_list:
        print(Fore.RED + "❌ No firmware files found.")
        return

    index = load_index()
    registered = {mod["file"]: mod for group in index for mod in group.get("modules", [])}

    for fw in fw_list:
        display_firmware(fw)
        if fw.replace(".docx", "").replace(".xlsx", "") in registered:
            print(Fore.GREEN + "✔ Indexed in firmware_index.json")
        else:
            print(Fore.RED + "✖ Not found in firmware_index.json")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="Regenerate firmware index")
    args = parser.parse_args()

    if args.refresh:
        regenerate_firmware_index()
    
    main()
