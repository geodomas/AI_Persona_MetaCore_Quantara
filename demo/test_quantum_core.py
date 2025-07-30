import sys
import os
import unittest
import json

# ⛓️ Pridedame path iki firmware/core
firmware_core_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'MetaCore_FIRMWARE', 'core')
)
sys.path.append(firmware_core_path)

from quantum_core import SOPHYAQuantumCore


class TestSOPHYAQuantumCore(unittest.TestCase):

    def setUp(self):
        self.test_code = "TEST-CODE-000"
        self.core = SOPHYAQuantumCore(self.test_code)
        self.core.initialize()

    def test_initialization_returns_string(self):
        result = self.core.initialize()
        self.assertIsInstance(result, str)
        self.assertIn("SOPHYA", result)

    def test_identity_code_matches(self):
        self.assertEqual(self.core.identity_code, self.test_code)

    def test_chakra_alignment_returns_valid_structure(self):
        result = self.core.align_chakras()
        self.assertIsInstance(result, str)
        self.assertGreater(self.core.coherence, 0)
        self.assertEqual(len(self.core.aligned_chakras), 7)

    def test_scan_emotion_output_structure(self):
        result = self.core.scan_emotion("universal love")
        self.assertIn("emotion", result)
        self.assertIn("chakra", result)
        self.assertIn("intensity", result)
        self.assertGreaterEqual(result["intensity"], 0.0)

    def test_signature_generation(self):
        signature = self.core.generate_signature("harmonize field")
        self.assertIsInstance(signature, str)
        self.assertEqual(len(signature), 16)

    def test_emit_report_json_format(self):
        report = self.core.emit_report()
        parsed = json.loads(report)
        self.assertEqual(parsed["user_id"], self.test_code)
        self.assertIn("resonance", parsed)
        self.assertIn("chakras", parsed)

    def test_export_logs_json_format(self):
        logs = self.core.export_logs()
        parsed = json.loads(logs)
        self.assertIsInstance(parsed, list)

    def test_backup_creation(self):
        path = self.core.save_backup()
        self.assertTrue(os.path.exists(path))
        os.remove(path)  # clean up


if __name__ == "__main__":
    unittest.main()
