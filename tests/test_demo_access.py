import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from demo_access import normalise_display_name


class DemoAccessTests(unittest.TestCase):
    def test_normalise_display_name_accepts_meaningful_name(self) -> None:
        self.assertEqual(normalise_display_name("  Bastien  "), "Bastien")

    def test_normalise_display_name_rejects_blank_value(self) -> None:
        self.assertIsNone(normalise_display_name("   "))


if __name__ == "__main__":
    unittest.main()
