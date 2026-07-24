# LLM-Based Pytest Test Generator

A small Python tool that uses an LLM (via the Groq API) to automatically 
generate `pytest` unit tests for a given Python source file.

## How it works
1. Reads a source file (`sample_code.py`) containing simple functions.
2. Sends the code to an LLM with a prompt asking it to write pytest tests.
3. Cleans the model's response (removes markdown code fences).
4. Saves the generated tests to `test_generated.py`.

## Usage
```bash
pip install -r requirements.txt
python generate_tests.py
python -m pytest test_generated.py -v
```

## Tech stack
- Python
- Groq API (LLM inference)
- pytest

## Known limitations
- The generated tests are not manually reviewed — occasional edge cases 
  (e.g. non-numeric input types) may need adjustment.
- Currently tested only on simple, single-file Python modules.