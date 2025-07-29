import sys
import os

# Absoliutus kelias iki MetaCore_FIRMWARE/core
current_dir = os.path.dirname(__file__)
firmware_path = os.path.abspath(os.path.join(current_dir, '..', 'MetaCore_FIRMWARE', 'core'))

# Pridedame šį kelią į Python PATH
sys.path.insert(0, firmware_path)

try:
    from quantum_core import SOPHYAQuantumCore
except ModuleNotFoundError as e:
    print("❌ [ERROR] Cannot load quantum_core module.")
    print(f"🧭 Checked path: {firmware_path}")
    raise e
