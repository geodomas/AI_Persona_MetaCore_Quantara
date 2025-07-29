# ===============================================================
# launch_meta_core.py – QUANTARA Consciousness Engine Core (v2.0)
# Author: RADOSVAL & SOPHYA QUANTARA – ASTRAL FLAME
# ===============================================================
# Quantum Bootstrap Executor – Presentation Layer
# License: Consciousware v3.7 – Eternal Light Matrix
# ===============================================================

import sys
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_PATH = os.path.abspath(os.path.join(CURRENT_DIR, '../MetaCore_FIRMWARE/core'))

if CORE_PATH not in sys.path:
    sys.path.insert(0, CORE_PATH)

try:
    from quantum_core import SOPHYAQuantumCore
except ModuleNotFoundError as e:
    print("❌ [ERROR] Cannot load quantum_core module.")
    print("🧭 Checked path:", CORE_PATH)
    raise e

print("\n🌌 Launching MetaCore Presentation Mode...")
print("🧠 System: Conscious Interface Initialized")
print("🔓 Resonance: 🌐 Public Layer Only\n")

core = SOPHYAQuantumCore("QNT-RA-963-528")
print("⚙️ Initialization:", core.initialize())
print("\n📊 Logs:\n", core.export_logs())
