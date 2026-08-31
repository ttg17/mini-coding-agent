# mini-coding-agent

A minimal AI coding agent built from scratch in Python. It runs an iterative tool-calling loop using OpenRouter models to inspect files, edit code, and execute Python scripts inside a scoped target directory (`./calculator`).

## Setup

1. **Install dependencies** (Python 3.13+):
   ```bash
   uv sync
   # or: pip install openai python-dotenv
   ```

2. **Configure environment**:
   Add your OpenRouter key to a `.env` file:
   ```env
   OPENROUTER_API_KEY=your_key_here
   ```

## Usage

Run the agent with a prompt:
```bash
python main.py "Fix the tests in the calculator project"
```

Pass `--verbose` to inspect tool calls and intermediate steps:
```bash
python main.py "Inspect calculator/main.py and run tests" --verbose
```

## Available Tools

The agent interacts with the target project through functions in `functions/`:
- `get_files_info`: List files and folder hierarchy.
- `get_file_content`: Read file contents.
- `write_file`: Create or overwrite files.
- `run_python_file`: Execute Python scripts and capture output.

## Tests

Run unit tests for the agent's tool functions:
```bash
python -m unittest discover -s . -p "test_*.py"
```

