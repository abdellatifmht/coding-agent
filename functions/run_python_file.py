import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    """
    Executes a Python file in the working directory and returns its output.

    The function runs the file with a 30-second timeout, captures both stdout
    and stderr, and returns a formatted string containing the return code,
    stdout, and stderr.

    Args:
        working_directory: The base directory from which to resolve the file path.
            The Python file must be within this directory tree.
        file_path: Path to the Python file to execute, relative to the
            working directory. Must end with ".py".
        args: Optional list of command-line arguments to pass to the Python file.
            Defaults to None (no arguments).

    Returns:
        A string containing the execution output, including:
        - Process return code (if non-zero)
        - STDOUT contents
        - STDERR contents
        - "No output produced." if the process produced nothing
        Or an error message if the file is outside the permitted directory,
        doesn't exist, isn't a Python file, or an exception occurs.

    Examples:
        >>> run_python_file(".", "calculator/main.py", ["3 + 5"])
        "STDOUT: {\"expression\": \"3 + 5\", \"result\": 8}\\n"

        >>> run_python_file(".", "missing.py")
        'Error: "missing.py" does not exist or is not a regular file'
    """
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        filename = os.path.basename(target_file)

        if not filename.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python3", target_file]

        if args:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        return_code = result.returncode
        output = ""

        if return_code != 0:
            output += f"Process exited with code {return_code}\n"

        if not result.stdout and not result.stderr:
            output += "No output produced.\n"

        if result.stdout:
            output += f"STDOUT: {result.stdout}\n"

        if result.stderr:
            output += f"STDERR: {result.stderr}\n"

        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file in the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python file",
                },
            },
        },
    },
}
