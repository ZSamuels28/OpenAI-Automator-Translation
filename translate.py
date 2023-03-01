import openai
import sys

# Read the API key
openai.api_key = [YOUR OPENAI API KEY]

# Get the selected text
selected_text = sys.stdin.read()

# Call the OpenAI API to translate the text
model = "gpt-3.5-turbo"
language = "Spanish"
response = openai.ChatCompletion.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": f"Translate the following text to {language} without changing the formatting: {selected_text}",
        }
    ]
)

# Grabs the response from the API and strips it of leading/trailing newlines
translated_text = response["choices"][0]["message"]["content"].strip()

# Replace the selected text with the translated text
sys.stdout.write(translated_text)
