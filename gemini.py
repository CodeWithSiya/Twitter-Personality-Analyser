import google.generativeai as genai
from dotenv import load_dotenv
import json
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

def load_tweets(filename : str) -> list:
    """
    Load tweets from a JSON file.

    :param: filename: Name of the JSON file containing tweets.

    Returns:
        List of Tweets with various metadata.
    """
    with (open(filename, "r", encoding = "utf-8")) as file:
        tweets_data = json.load(file)

    tweets = [tweet['text'] for tweet in tweets_data]
    return tweets

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
    tweets = load_tweets("tweets.json")
    for tweet in tweets:
        print(tweet)
    # model = configure_model()
    # prompt = input("Enter a prompt:\n")
    # response = model.generate_content(prompt)
    # print(response.text)

if __name__ == "__main__":
    main()