import google.generativeai as genai
from dotenv import load_dotenv
import os

"""
Gemini Generative AI API Authentication and Configuration.

Author: Siyabonga Madondo
Version: 16/07/2024
"""

def load_credentials() -> dict:
    """
    Load Twitter API credentials from the .env file.

    Returns:
        A dictionary containing loaded credentials.
    """
    load_dotenv()
    return {
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
    }

def configure_model() -> genai.GenerativeModel:
    """
    Initialize and configure the generative ai model.

    Returns:
        The initialized model.
    """
    credentials = load_credentials()
    genai.configure(api_key = credentials["GOOGLE_API_KEY"])
    return genai.GenerativeModel('gemini-1.5-flash')

def main():
    model = configure_model()
    prompt = input("Enter a prompt:\n")
    response = model.generate_content(prompt)
    print(response.text)

if __name__ == "__main__":
    main()