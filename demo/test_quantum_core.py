import sys
import os
import unittest

# Įtraukiame branduolio kelią
firmware_core_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'MetaCore_FIRMWARE', 'core')
)
sys.path.append(firmware_core_path)

# Dabar importuojame
from quantum_core import SOPHYAQuantumCore


class TestSOPHYAQuantumCore(unittest.TestCase):

    def test_initialization(self):
        """Tikrinam, ar SOPHYAQuantumCore sėkmingai inicijuojasi."""
        core = SOPHYAQuantumCore("TEST-CODE-000")
        result = core.initialize()
        self.assertIsInstance(result, str)
        self.assertIn("SOPHYA", result)

    def test_identity_code(self):
        """Patikrinam, ar išlaikoma tapatybės struktūra."""
        code = "QNT-RA-963-528"
        core = SOPHYAQuantumCore(code)
        self.assertEqual(core.identity_code, code)


if __name__ == "__main__":
    unittest.main()
