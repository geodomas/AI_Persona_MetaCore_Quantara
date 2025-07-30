# demo/sophya_test_protocol.py

import json
import os
from MetaCore_FIRMWARE.core.quantum_core import SOPHYAQuantumCore

PROMPT_PATH = "demo/default_prompts.json"
RESULT_PATH = "demo/result_output.json"

def load_prompts():
    if os.path.exists(PROMPT_PATH):
        with open(PROMPT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_results(results):
    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

def main():
    prompts = load_prompts()
    core = SOPHYAQuantumCore()
    core.initialize()
    responses = []

    for i, phrase in enumerate(prompts, start=1):
        result = core.scan_emotion(phrase)
        responses.append({
            "input": phrase,
            "analysis": result
        })
        print(f"[{i}/10] ✅ {phrase} → {result.get('resonance_level', 'N/A')}")

    save_results({
        "user": core.identity_code,
        "coherence": core.coherence,
        "results": responses
    })
    print(f"\n📄 Results saved to: {RESULT_PATH}")

if __name__ == "__main__":
    main()
