# calculator/pkg/calculator.py

from collections.abc import Callable


class Calculator:
    """A simple infix expression evaluator that supports basic arithmetic operators.

    The calculator parses space-separated tokens and evaluates expressions
    using the standard operator precedence (multiplication and division before
    addition and subtraction).
    """

    def __init__(self) -> None:
        """Initializes the Calculator with supported operators and their precedences."""
        self.operators: dict[str, Callable[[float, float], float]] = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence: dict[str, int] = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression: str) -> float | None:
        """Evaluates an infix arithmetic expression and returns the result.

        Args:
            expression: A space-separated infix arithmetic expression
                (e.g., "3 + 5 * 2").

        Returns:
            The computed result as a float, or None if the expression
            is empty or contains only whitespace.

        Raises:
            ValueError: If the expression contains invalid tokens or
                is malformed (e.g., not enough operands).

        Examples:
            >>> calc = Calculator()
            >>> calc.evaluate("3 + 5")
            8
            >>> calc.evaluate("2 * 3 - 8 / 2 + 5")
            7
            >>> calc.evaluate("")
        """
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens: list[str]) -> float:
        """Evaluates a list of space-separated tokens using a shunting-yard algorithm.

        Processes tokens left to right, applying operator precedence rules
        to compute the final value.

        Args:
            tokens: A list of space-separated tokens representing
                numbers and operators (e.g., ["3", "+", "5"]).

        Returns:
            The computed result as a float.

        Raises:
            ValueError: If a token cannot be parsed as a number,
                or if the expression is malformed (e.g., not enough
                operands when applying an operator).
        """
        values: list[float] = []
        operators: list[str] = []

        for token in tokens:
            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators: list[str], values: list[float]) -> None:
        """Pops an operator and two values, applies the operator, and pushes the result back.

        Args:
            operators: The stack of operator tokens.
            values: The stack of numeric values.

        Raises:
            ValueError: If there are not enough operands to apply the operator,
                or if the operator stack is empty.
        """
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))