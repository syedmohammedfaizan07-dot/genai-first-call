from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()

# Get OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("OpenRouter API key is missing")

# Connect to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# Send request to AI model
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Explain Generative AI in simple terms in three bullet points."
        }
    ]
)

# Display AI response
print(response.choices[0].message.content)