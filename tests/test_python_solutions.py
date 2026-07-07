import importlib
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))


class QuestionOneTests(unittest.TestCase):
    def test_convert_temp_converts_known_values_and_rejects_unknown_units(self):
        q1 = importlib.import_module("q1_python")

        self.assertEqual(q1.convertTemp(100, "C"), 212.0)
        self.assertEqual(q1.convertTemp(32, "F"), 0.0)
        self.assertEqual(q1.convertTemp(37, "C"), 98.6)
        self.assertEqual(q1.convertTemp("invalid", "X"), -1)

    def test_convert_temp_rounds_to_two_decimal_places(self):
        q1 = importlib.import_module("q1_python")

        self.assertEqual(q1.convertTemp(98.6, "F"), 37.0)
        self.assertEqual(q1.convertTemp(0, "C"), 32.0)


class QuestionTwoTests(unittest.TestCase):
    def setUp(self):
        if "q2_python" in sys.modules:
            del sys.modules["q2_python"]
        self.q2 = importlib.import_module("q2_python")
        self.q2.inventory.clear()

    def test_add_item_stores_unique_items_and_warns_for_duplicates(self):
        output = io.StringIO()

        with redirect_stdout(output):
            self.q2.addItem("Laptop")
            self.q2.addItem("Mouse")
            self.q2.addItem("Keyboard")
            self.q2.addItem("Mouse")

        self.assertEqual(self.q2.inventory, ["Laptop", "Mouse", "Keyboard"])
        self.assertIn("Mouse is already in inventory.", output.getvalue())

    def test_list_inventory_prints_items_or_empty_message(self):
        empty_output = io.StringIO()
        with redirect_stdout(empty_output):
            self.q2.listInventory()
        self.assertEqual(empty_output.getvalue().strip(), "Inventory is empty.")

        self.q2.inventory.extend(["Laptop", "Mouse"])
        filled_output = io.StringIO()
        with redirect_stdout(filled_output):
            self.q2.listInventory()
        self.assertEqual(filled_output.getvalue().strip(), "Inventory: ['Laptop', 'Mouse']")


class QuestionThreeTests(unittest.TestCase):
    def test_format_name_returns_title_cased_last_first(self):
        q3 = importlib.import_module("q3_python")

        self.assertEqual(q3.formatName("Alice", "Tan"), "Tan, Alice")
        self.assertEqual(q3.formatName("bob", "lim"), "Lim, Bob")
        self.assertEqual(q3.formatName("MARY", "o'connor"), "O'Connor, Mary")

    def test_format_initials_returns_uppercase_initials(self):
        q3 = importlib.import_module("q3_python")

        self.assertEqual(q3.formatInitials("Alice", "Tan"), "A.T.")
        self.assertEqual(q3.formatInitials("bob", "lim"), "B.L.")
        self.assertEqual(q3.formatInitials("mARY", "o'connor"), "M.O.")


if __name__ == "__main__":
    unittest.main()
