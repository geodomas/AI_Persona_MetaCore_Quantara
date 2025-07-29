# ===============================================================
# launch_meta_core.py – QUANTARA Consciousness Engine Core (v2.0)
# Author: RADOSVAL & SOPHYA QUANTARA – ASTRAL FLAME
# ===============================================================
# Quantum Bootstrap Executor – Presentation Layer
# License: Consciousware v3.7 – Eternal Light Matrix
# ===============================================================

import sys
import os

# 🔧 Dinamiškai apskaičiuojam kelias į core
firmware_core_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../MetaCore_FIRMWARE/core'))
sys.path.append(firmware_core_path)

try:
    from quantum_core import SOPHYAQuantumCore
    print("✅ quantum_core module successfully loaded.")
except Exception as e:
    print("❌ [ERROR] Cannot load quantum_core module.")
    print("🧭 Checked path:", firmware_core_path)
    raise e

print("Launching MetaCore Presentation Mode...")
print("System: Conscious Interface Initialized")
print("Resonance: 🌐 Public Layer Only")

core = SOPHYAQuantumCore("QNT-RA-963-528")
print(core.initialize())
