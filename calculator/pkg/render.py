# calculator/pkg/render.py

import json


def format_json_output(expression: str, result: float, indent: int = 2) -> str:
    """
    Formats a calculator expression evaluation as a JSON object.

    The function converts the numeric result to an integer when it is
    mathematically equivalent to one (e.g., 8.0 becomes 8). It then builds
    a dictionary with keys "expression" and "result" and serializes it as
    pretty-printed JSON.

    Args:
        expression: The original arithmetic expression (e.g., "3 + 5").
        result: The computed numeric result (float).
        indent: Number of spaces for indentation in the JSON output (default 2).

    Returns:
        A JSON-formatted string containing the expression and its result.

    Examples:
        >>> format_json_output("3 + 5", 8)
        '{"expression": "3 + 5", "result": 8}'

        >>> format_json_output("2 * 3 - 8 / 2 + 5", 7)
        '{"expression": "2 * 3 - 8 / 2 + 5", "result": 7}'
    """
    if isinstance(result, float) and result.is_integer():
        result_to_dump = int(result)
    else:
        result_to_dump = result

    output_data = {
        "expression": expression,
        "result": result_to_dump,
    }
    return json.dumps(output_data, indent=indent)