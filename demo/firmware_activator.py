import json
import os

FIRMWARE_INDEX = "MetaCore_FIRMWARE/config/firmware_index.json"
FIRMWARE_CORE = "MetaCore_FIRMWARE/core"

def load_index():
    with open(FIRMWARE_INDEX, "r", encoding="utf-8") as f:
        data = json.load(f)
        # Tikriname ar kiekvienas įrašas tikrai dict
        return [json.loads(item) if isinstance(item, str) else item for item in data]

def activate_firmware(meta):
    print(f"\n🔮 Activating: {meta['firmware_name']}")
    print(f"📌 MODULE: {meta.get('Module')}")
    print(f"🧠 COMMAND: {meta.get('COMMAND')}")
    print(f"🛠️ SYSTEM: {meta.get('System')}")
    print("-" * 50)

def main():
    firmware_index = load_index()
    for meta in firmware_index:
        if meta.get("AUTO_START", "").strip().upper() == "ON":
            activate_firmware(meta)

if __name__ == "__main__":
    main()
