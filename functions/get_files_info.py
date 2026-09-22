import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    """
    Lists files and subdirectories in a specified directory relative to
    the working directory, providing each entry's file size and whether
    it is a directory.

    Args:
        working_directory: The base directory from which to resolve the path.
            Access outside this directory is blocked for security reasons.
        directory: Path to the directory to list files from, relative to the
            working directory. Defaults to "." (the working directory itself).

    Returns:
        A newline-separated string where each entry has the format:
            - <name>: file_size=<size> bytes, is_dir=<True|False>
        Or an error message if the directory is outside the permitted
        working directory, doesn't exist, or an exception occurs.

    Examples:
        >>> get_files_info(".", "src")
        "- utils.py: file_size=1234 bytes, is_dir=False\\n- helpers: file_size=4096 bytes, is_dir=True"

        >>> get_files_info(".", "/etc")
        'Error: Cannot list "/etc" as it is outside the permitted working directory'
    """
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        files_info = []

        for entry in os.listdir(target_dir):
            entry_path = os.path.join(target_dir, entry)
            size = os.path.getsize(entry_path)
            is_directory = os.path.isdir(entry_path)
            files_info.append(
                f"- {entry}: file_size={size} bytes, is_dir={is_directory}"
            )

        return "\n".join(files_info)

    except Exception as e:
        return f'Error: {e}'


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
