import ollama
import re


def clean_filename(name):

    name = re.sub(r'[^a-zA-Z0-9_ ]', '', name)

    name = name.replace(" ", "_")

    return name[:50]



def generate_filename(text, label):

    short_text = text[:1200]

    prompt = f"""
Generate ONLY a short filename.

Rules:
- Maximum 4 words
- Use underscores
- No explanation
- No sentences
- Filename only

Examples:
Bank_Statement
OS_Assignment
Amazon_Order

Document:
{short_text}
"""

    try:

        response = ollama.chat(
            model='mistral',
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        filename = response['message']['content']

        filename = filename.splitlines()[0].strip()

        filename = clean_filename(filename)

        if not filename:
            filename = label + "_Document"

        return filename

    except Exception as e:

        print("Ollama Error:", e)

        return label + "_Document"