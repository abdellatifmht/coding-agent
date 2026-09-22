import json

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python_file import schema_run_python_file, run_python_file
from collections.abc import Callable

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
]


def call_function(tool_call, verbose: bool = False) -> dict:
    """
    Executes a function specified by a tool call from the AI model.

    Parses the function name and arguments from the tool call,
    looks up the corresponding implementation, executes it, and
    returns a tool message containing the result.

    Args:
        tool_call: An object containing the function name, arguments,
            and tool call ID (e.g., from an OpenAI tool call response).
        verbose: If True, prints the function name and its arguments
            before execution. Defaults to False.

    Returns:
        A dictionary representing a tool message with:
            - "role": "tool"
            - "tool_call_id": The ID from the tool call
            - "content": The function result as a string, or an
              error message if the function name is unknown

    Raises:
        json.JSONDecodeError: If the function arguments are not
            valid JSON.
        KeyError: If the tool_call object doesn't have the expected
            structure.

    Examples:
        >>> call_function(tool_call, verbose=False)
        {'role': 'tool', 'tool_call_id': 'call_abc123', 'content': '- file.py: file_size=100 bytes, is_dir=False'}
    """

    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")

    if verbose:
        print(f" - Calling function: {function_name}({function_args})")

    else:
        print(f" - Calling function: {function_name}")

    function_map: dict[str, Callable[..., str]] = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }

    function_args["working_directory"] = "."

    result = function_map[function_name](**function_args)

    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }
