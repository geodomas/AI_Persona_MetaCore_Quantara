import sys
import os

# Pridedame tikslų kelią iki quantum_core.py
current_dir = os.path.dirname(__file__)
firmware_path = os.path.abspath(os.path.join(current_dir, '..', 'MetaCore_FIRMWARE', 'core'))
sys.path.insert(0, firmware_path)

print(f"🔍 Checking import path: {firmware_path}")
print("📂 Files in path:", os.listdir(firmware_path))

try:
    from quantum_core import SOPHYAQuantumCore
    print("✅ Import successful!")
except Exception as e:
    print("❌ Import failed:", e)
