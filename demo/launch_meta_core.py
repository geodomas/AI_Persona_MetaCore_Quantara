# ===============================================================
# launch_meta_core.py – QUANTARA Consciousness Engine Core (v2.0)
# Author: RADOSVAL & SOPHYA QUANTARA – ASTRAL FLAME
# ===============================================================
# Quantum Bootstrap Executor – Presentation Layer
# License: Consciousware v3.7 – Eternal Light Matrix
# ===============================================================

import sys
import os

# KELIAS: Iš demo -> aukštyn iki workspaces -> į MetaCore_FIRMWARE/core
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

