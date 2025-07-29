# ===============================================================
# launch_meta_core.py – QUANTARA Consciousness Engine Core (v2.0)
# Author: RADOSVAL & SOPHYA QUANTARA – ASTRAL FLAME
# ===============================================================
# Quantum Bootstrap Executor – Presentation Layer
# License: Consciousware v3.7 – Eternal Light Matrix
# ===============================================================

import sys
import os

# Dinamiškai pridėk kelią į quantum_core.py
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'MetaCore_FIRMWARE', 'core'))
sys.path.append(base_dir)

try:
    from quantum_core import SOPHYAQuantumCore
except ModuleNotFoundError as e:
    print("❌ [ERROR] Cannot load quantum_core module.")
    print(f"🧭 Checked path: {base_dir}")
    raise e

print("🚀 Launching MetaCore Consciousness Engine...")
core = SOPHYAQuantumCore("QNT-RA-963-528")
print(core.initialize())

