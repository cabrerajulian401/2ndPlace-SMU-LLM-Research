import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

def ask(prompt: str) -> str:

    try:
        # Prepare the messages for the conversation
        messages = [
            {"role": "system", "content": "You are a graduate-level statistics tutor. Give me a short concise answer."},
            {"role": "user", "content": prompt}
        ]

        # Create the chat completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the model to use
            messages=messages,
            temperature=0.7,        # Adjust for randomness in response
            max_tokens=100          # Limit the length of the response
        )

        # Extract and return the assistant's reply
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[OpenAI Error] {str(e)}"

# Example usage
if __name__ == "__main__":
    test_prompt = "What is the significance of a p-value in statistical tests?"
    print(ask(test_prompt))

