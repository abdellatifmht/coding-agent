import os
from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    """
    Reads the content of a specified file relative to the working directory,
    returning the content as a string. The file content is limited to MAX_CHARS
    characters, and if the file exceeds this limit, a truncation notice is added.

    Args:
        working_directory: The base directory from which to resolve the file path.
            Files outside this directory cannot be accessed for security reasons.
        file_path: Path to the file to read, relative to the working directory.
            Can include subdirectories (e.g., "subdir/file.txt").

    Returns:
        The file content as a string, or an error message if:
        - The file is outside the permitted working directory
        - The file doesn't exist or is not a regular file
        - An exception occurs during reading

    Examples:
        >>> get_file_content(".", "README.md")
        "# Project Title\\n\\nThis is a project..."

        >>> get_file_content("/home/user/docs", "file.txt")
        "Error: File not found or is not a regular file: \"file.txt\""
    """
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, 'r') as file:
            content = file.read(MAX_CHARS)

            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content

    except Exception as e:
        return f'Error: {e}'


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the content of a specified file relative to the working directory, returning the content as a string",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
        },
    },
}
