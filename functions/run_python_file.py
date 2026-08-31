import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        command = ["python", target_dir]
        if args:
            command.extend(args)

        process = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
            check=False
        )

        result = ''
        result += f"Process exited with code {process.returncode}\n"
        if not process.stderr and not process.stdout:
            result += "No output produced\n"
        else:
            result += f"STDOUT: {process.stdout}\n"
            result += f"STDERR: {process.stderr}\n"

        return result

    except Exception as e:  # noqa: BLE001
        return f"Error: executing Python file: {e}\n"



schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the python file that is to be run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script"
                }
            },
            "required": ["file_path"],
        },
    },
}