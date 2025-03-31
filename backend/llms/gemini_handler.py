import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv


def ask(question: str) -> str:
    # Load the API key from the environment variable
    
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    if GOOGLE_API_KEY is None:
        return "[Gemini Error] GOOGLE_API_KEY environment variable not set."
    
    # Configure the API key
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Initialize the Gemini model (adjust the model name if necessary)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Prepend your system instruction to the question
    system_prompt = "Answer this multiple choice question as a high quality graduate statistics student taking an exam. Give me a short concise answer. "
    full_prompt = system_prompt + "Question: " + question

    


    try:
        # Generate the response using the Gemini model
        response = model.generate_content(full_prompt)




        return response.text.strip() if response.text else "[No answer returned]"
    except Exception as e:
        return f"[Gemini Error] {str(e)}"

# For testing purposes:
if __name__ == "__main__":
    test_question = "What is a p-value?"
    print(ask(test_question))
