# Calculator

A command-line calculator that evaluates mathematical expressions with proper operator precedence.

## Description

This project implements a simple calculator that can evaluate mathematical expressions including addition, subtraction, multiplication, and division. The calculator supports operator precedence and handles nested expressions. It provides a clean command-line interface and outputs results in JSON format.

## Features

- **Basic Operations**: Addition (+), subtraction (-), multiplication (*), and division (/)
- **Operator Precedence**: Proper handling of mathematical order of operations (e.g., 2 * 3 + 5 = 11, not 16)
- **Nested Expressions**: Support for complex expressions with multiple operators
- **Clean CLI**: Simple command-line interface with helpful usage instructions
- **JSON Output**: Results formatted as structured JSON for easy parsing
- **Comprehensive Testing**: Full test suite with unit tests covering edge cases
- **Error Handling**: Robust error handling for invalid expressions and operators

## Project Structure

```
calculator/
├── main.py          # Command-line interface
├── tests.py         # Unit tests
├── pkg/
│   ├── calculator.py  # Core calculator implementation
│   ├── render.py      # JSON output formatting
└── README.md        # Project documentation
```

## Requirements / Prerequisites

- Python 3.7 or higher
- No external dependencies required (pure Python implementation)

## Installation

No special installation is required. This project uses only the Python standard library, so you can run it directly after cloning the repository.

```bash
git clone <repository-url>
cd calculator
```

## Usage

### Command Line Interface

Run the calculator from the command line:

```bash
python main.py "<expression>"
```

**Examples:**
```bash
python main.py "3 + 5"
python main.py "10 / 2"
python main.py "2 * 3 - 8 / 2 + 5"
```

### Without Arguments

If no expression is provided, the calculator will display usage information:

```bash
python main.py
```

**Output:**
```
Calculator App
Usage: python main.py "<expression>"
Example: python main.py "3 + 5"
```

### Output Format

The calculator outputs results in JSON format:

```json
{
  "expression": "3 + 5",
  "result": 8
}
```

## Examples

### Basic Operations
```bash
python main.py "3 + 5"
# Output: {"expression": "3 + 5", "result": 8}

python main.py "10 - 4"
# Output: {"expression": "10 - 4", "result": 6}

python main.py "3 * 4"
# Output: {"expression": "3 * 4", "result": 12}

python main.py "10 / 2"
# Output: {"expression": "10 / 2", "result": 5}
```

### Complex Expressions
```bash
python main.py "3 * 4 + 5"
# Output: {"expression": "3 * 4 + 5", "result": 17}

python main.py "2 * 3 - 8 / 2 + 5"
# Output: {"expression": "2 * 3 - 8 / 2 + 5", "result": 7}
```

### Error Handling
```bash
python main.py "3 +"
# Output: Error: not enough operands for operator +

python main.py "$ 3 5"
# Output: Error: invalid token: $
```

## How to Run Tests

To run the unit tests and verify the calculator's functionality, use Python's built-in `unittest` module:

```bash
python tests.py
```

Or, if you prefer `pytest`:

```bash
python -m pytest tests.py
```

## License

This project is open source. Please see the LICENSE file for licensing information.
