# tools/generate_firmware_methods.py

import json
import os

INDEX_PATH = "MetaCore_FIRMWARE/config/firmware_index.json"
OUTPUT_PATH = "MetaCore_FIRMWARE/core/firmware_methods.py"

def snake_case(name):
    return name.lower().replace(" ", "_").replace("-", "_")

def generate_method(module):
    name = module.get("file", "unknown").replace("firmware_", "").replace(".docx", "")
    func_name = snake_case(name)
    description = module.get("name", "Firmware Module")
    return f"""
def {func_name}(self):
    self.log_event("firmware_{func_name}", {{"status": "active"}})
    return "⚙️ {description} activated."
""".strip()

def main():
    with open(INDEX_PATH, "r") as f:
        index_data = json.load(f)

    methods = []
    for group in index_data:
        for mod in group.get("modules", []):
            methods.append(generate_method(mod))

    content = "# Auto-generated firmware methods\n\n" + "\n\n".join(methods) + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Generated {len(methods)} methods in: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
