"""Small validation tests for translation data; does not test DFHack integration."""
from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TranslationDataTests(unittest.TestCase):
    def test_core_csv_has_unique_nonempty_source_keys(self) -> None:
        path = ROOT / "translation" / "dictionaries" / "core.csv"
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertTrue(rows, "dictionary should contain seed rows")
        sources = [row["source"].strip() for row in rows]
        self.assertTrue(all(sources), "source keys must not be empty")
        self.assertEqual(len(sources), len(set(sources)), "duplicate source keys found")
        self.assertTrue(all(row["target"].strip() for row in rows), "translation targets must not be empty")

    def test_transliteration_json_is_valid_and_has_maps(self) -> None:
        path = ROOT / "translation" / "rules" / "transliteration.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], 1)
        self.assertIn("letters", data)
        self.assertIn("digraphs", data)
        self.assertIn("sh", data["digraphs"])
        self.assertIn("a", data["letters"])


if __name__ == "__main__":
    unittest.main()
