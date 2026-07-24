import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 1. Read the source code to generate tests for
with open("sample_code.py", "r") as f:
    source_code = f.read()

# 2. Build the prompt to ask the model for pytest tests
prompt = f"""Write a complete pytest test file for the following Python code.
The code is in a file called sample_code.py.
Start the test file with: from sample_code import *
Only output valid Python code. Do NOT wrap it in markdown code blocks or triple backticks. Do NOT add any explanation text.

Code:
{source_code}
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

generated_tests = response.choices[0].message.content

# Clean up: remove markdown code fences (```python and ```) if the model added them
generated_tests = generated_tests.strip()
if generated_tests.startswith("```"):
    lines = generated_tests.split("\n")
    lines = lines[1:]  # remove the opening ```python line
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]  # remove the closing ``` line
    generated_tests = "\n".join(lines)

with open("test_generated.py", "w") as f:
    f.write(generated_tests)

print("Done! open test_generated.py")