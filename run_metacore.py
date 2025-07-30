# run_sophya.py
from MetaCore_FIRMWARE.core.quantum_core import SOPHYAQuantumCore

core = SOPHYAQuantumCore()
print(core.initialize())
print(core.align_chakras())
print(core.scan_emotion("harmonija ir drąsa"))
print(core.save_backup())
core.boot_auto_start_modules()
