import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    """
    Writes content to a specified file relative to the working directory.

    Creates parent directories as needed and ensures the target path is within
    the permitted working directory. Raises errors for invalid paths or
    permission issues.

    Args:
        working_directory: The base directory from which to resolve the file path.
            All writes must stay within this directory tree.
        file_path: Path to the file to write, relative to the working directory.
            Parent directories will be created automatically if they don't exist.
        content: The string content to write to the file.

    Returns:
        A success message indicating how many characters were written, or
        an error message if the operation failed.

    Examples:
        >>> write_file(".", "hello.txt", "Hello, world!")
        "Successfully wrote to \"hello.txt\" (18 characters written)"

        >>> write_file(".", "out_of_bounds.txt", "data")
        "Error: Cannot write to \"out_of_bounds.txt\" as it is outside the permitted working directory"
    """
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file",
                },
            },
        },
    },
}
