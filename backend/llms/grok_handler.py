import os
import requests
from dotenv import load_dotenv


def ask(prompt: str) -> str:
    """
    Sends a prompt to the Grok-2 model and returns the response.

    :param prompt: The textual prompt to send to the model.
    :return: The model's response as a string.
    """
    try:
        # Define the API endpoint

        load_dotenv()
        url = "https://api.x.ai/v1/chat/completions"

        # Hard coded remove later 
        api_key = os.getenv("XAI_API_KEY")
        if not api_key:
            return "[Grok Error] XAI_API_KEY environment variable not set."

        # Set up the headers for the request
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Prepare the payload
        payload = {
            "model": "grok-2-1212",  # Ensure this model identifier is valid
            "messages": [
                {"role": "system", "content": "You are a graduate-level statistics tutor. Give me a short concise answer.s"},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 100  # Adjust as needed
        }

        # Send the POST request to the API
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        # Parse and return the content from the response
        return response.json()['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"[Grok Error] {str(e)}"

# Example usage:
if __name__ == "__main__":
    test_prompt = "What is the significance of a p-value in statistical tests?"
    print(ask(test_prompt))


