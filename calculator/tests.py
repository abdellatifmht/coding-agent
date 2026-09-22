# calculator/tests.py

import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Unit tests for the Calculator class.

    Verifies that the calculator correctly handles basic arithmetic
    operations, operator precedence, nested expressions, and invalid
    input cases.
    """

    def setUp(self) -> None:
        """Sets up a fresh Calculator instance before each test."""
        self.calculator = Calculator()

    def test_addition(self) -> None:
        """Tests that the calculator correctly evaluates addition expressions."""
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self) -> None:
        """Tests that the calculator correctly evaluates subtraction expressions."""
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self) -> None:
        """Tests that the calculator correctly evaluates multiplication expressions."""
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self) -> None:
        """Tests that the calculator correctly evaluates division expressions."""
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self) -> None:
        """Tests that the calculator correctly applies operator precedence in a nested expression."""
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self) -> None:
        """Tests that the calculator correctly evaluates a complex expression with multiple operators."""
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_empty_expression(self) -> None:
        """Tests that the calculator returns None for an empty expression."""
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self) -> None:
        """Tests that the calculator raises ValueError for invalid operators."""
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self) -> None:
        """Tests that the calculator raises ValueError when an operator lacks enough operands."""
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")


if __name__ == "__main__":
    unittest.main()