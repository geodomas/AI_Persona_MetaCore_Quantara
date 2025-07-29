import sys
import os

firmware_core_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'MetaCore_FIRMWARE', 'core'))
print(f"🔍 Adding firmware_core_path: {firmware_core_path}")
sys.path.append(firmware_core_path)

try:
    from quantum_core import SOPHYAQuantumCore
    print("✅ Import successful from launch_meta_core.py")
except ModuleNotFoundError as e:
    print("❌ [ERROR] Cannot load quantum_core module.")
    print(f"🧭 Checked path: {firmware_core_path}")
    raise e

print("🚀 Launching MetaCore Consciousness Engine...")
core = SOPHYAQuantumCore("QNT-RA-963-528")
print(core.initialize())
