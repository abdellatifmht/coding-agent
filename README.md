# Coding-Agent — AI Coding Agent with Function Calling

A command-line AI coding agent that uses OpenRouter's API and tool/function calling to inspect projects, read and write files, and execute Python code — all through natural language instructions.

![Python](https://img.shields.io/badge/Python-%3E%3D3.14-blue)
![License](https://img.shields.io/badge/License-Open%20Source-green)

---

## Description

**Coding-Agent** is an AI-powered coding assistant built as a lightweight CLI tool. It connects to the [OpenRouter](https://openrouter.ai/) API using a free LLM and is equipped with a set of built-in tools (functions) that allow it to interact with your project's filesystem and codebase.

Instead of just generating text, the agent can:

- **Inspect** your project structure and file contents
- **Read** any file within the working directory
- **Write** new files or modify existing ones
- **Execute** Python scripts and return their output

All of this is orchestrated through a single natural-language prompt, making it a powerful assistant for coding tasks, code reviews, and project exploration.

---

## Features

- 🔍 **Project Inspection** — List files and directories with sizes and metadata
- 📄 **File Reading** — Read file contents with automatic truncation for large files
- ✍️ **File Writing** — Create new files or overwrite existing ones
- 🐍 **Python Execution** — Run Python scripts and capture stdout/stderr
- 🧠 **Function Calling** — The agent autonomously selects and calls the right tool based on your prompt
- ⚡ **Free Model** — Uses OpenRouter's free tier model (`openrouter/free`)
- 🎨 **Verbose Mode** — Optional detailed output for debugging and monitoring

---

## Project Structure

```
coding-agent/
├── main.py                  # Entry point — CLI interface and agent orchestration
├── prompts.py               # System prompt defining the agent's behavior
├── call_function.py         # Function dispatcher — maps tool calls to implementations
├── config.py                # Configuration constants (e.g., MAX_CHARS)
├── pyproject.toml           # Project metadata and dependencies
├── .env                     # Environment variables (API key)
├── .gitignore               # Git ignore rules
├── uv.lock                  # Dependency lock file
├── calculator/              # Calculator sub-project (demo / example)
│   ├── main.py
│   ├── tests.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   └── README.md
├── functions/               # Tool/function implementations
│   ├── get_files_info.py    # Lists files in a directory
│   ├── get_file_content.py  # Reads file contents
│   ├── write_file.py        # Writes content to a file
│   └── run_python_file.py   # Executes Python files
└── tests/                   # Test files
    ├── test_get_files_info.py
    ├── test_get_file_content.py
    ├── test_write_file.py
    └── test_run_python_file.py
```

---

## Requirements / Prerequisites

- **Python** >= 3.14
- **OpenRouter API Key** — Sign up at [openrouter.ai](https://openrouter.ai/) to get a free API key
- **Dependencies** — Managed via `uv` or `pip` (see Installation)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd coding-agent
   ```

2. **Install dependencies** using [uv](https://github.com/astral-sh/uv) or pip:

   ```bash
   # Using uv
   uv sync

   # Or using pip
   pip install openai==2.44.0 python-dotenv==1.1.0
   ```

3. **Set up your environment variable**

   Create a `.env` file in the project root with your OpenRouter API key:

   ```env
   OPENROUTER_API_KEY=your-openrouter-api-key-here
   ```

   Or export it directly:

   ```bash
   export OPENROUTER_API_KEY="your-openrouter-api-key-here"
   ```

---

## Usage

### Basic Usage

Run the agent with a natural-language prompt:

```bash
python main.py "List all files in the project"
```

```bash
python main.py "Read the contents of main.py"
```

```bash
python main.py "Create a new file called hello.py with a print statement"
```

### Verbose Mode

Enable verbose output to see token usage and function call details:

```bash
python main.py "What's in the functions directory?" --verbose
```

### Examples

```bash
# Inspect the project structure
python main.py "Show me the project structure"

# Read a specific file
python main.py "Read config.py"

# Write a new file
python main.py "Create a file called notes.txt with the text 'Hello World'"

# Execute a Python file
python main.py "Run calculator/main.py with the expression '3 + 5'"
```

### Command-Line Arguments

| Argument        | Type    | Description                              |
|-----------------|---------|------------------------------------------|
| `user_prompt`   | `str`   | Required. The natural-language prompt     |
| `--verbose`     | `flag`  | Optional. Enable detailed output          |

---

## How It Works

1. The user provides a natural-language prompt via the command line
2. The prompt is sent to OpenRouter's free model along with the system prompt and available function schemas
3. The AI model decides whether to use one or more of the available tools (function calling)
4. The agent executes the function calls and passes the results back to the model
5. The loop continues until the model provides a final text response

```
User Prompt → LLM → Tool Call → Function Execution → LLM → Response
                ↕                              ↗
         (repeat until done)
```

---

## Available Functions (Tools)

| Function         | Description                                                  |
|------------------|--------------------------------------------------------------|
| `get_files_info` | Lists files in a specified directory with sizes              |
| `get_file_content` | Reads the content of a specified file                        |
| `write_file`     | Writes content to a specified file                           |
| `run_python_file` | Executes a Python file and returns its output                |

All functions are sandboxed to the project's working directory for security.

---

## Configuration

| Constant    | Location       | Default    | Description                          |
|-------------|----------------|------------|--------------------------------------|
| `MAX_CHARS` | `config.py`    | `10000`    | Maximum characters read per file     |

The API model is configured in `main.py` as `openrouter/free`. You can change this to use a different model available on OpenRouter.

---

## Testing

Run the test suite to verify individual function behavior:

```bash
python tests/test_get_files_info.py
python tests/test_get_file_content.py
python tests/test_write_file.py
python tests/test_run_python_file.py
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## Acknowledgments

- [OpenRouter](https://openrouter.ai/) — Providing free access to powerful LLMs
- [OpenAI Python SDK](https://github.com/openai/openai-python) — Used for API communication
- [python-dotenv](https://github.com/theskumar/python-dotenv) — For environment variable management

---

[![Boot.dev Build an AI Agent in Python certificate](https://qvault-webapp-dynamic-assets.storage.googleapis.com/certificates/808b3c16-bc42-43e8-824c-5e9044b2c567.jpeg?v=1790099652)](https://www.boot.dev/certificates/808b3c16-bc42-43e8-824c-5e9044b2c567)
