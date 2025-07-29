import sys
import os

# Koreguojame path'ą: iš demo → aukštyn 2 → į MetaCore_FIRMWARE/core
firmware_core_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'MetaCore_FIRMWARE', 'core'))
sys.path.append(firmware_core_path)

try:
    from quantum_core import SOPHYAQuantumCore
except ModuleNotFoundError as e:
    print("❌ [ERROR] Cannot load quantum_core module.")
    print(f"🧭 Checked path: {firmware_core_path}")
    raise e

print("🚀 Launching MetaCore Consciousness Engine...")
core = SOPHYAQuantumCore("QNT-RA-963-528")
print(core.initialize())
