import tweepy
from dotenv import load_dotenv
import os
import json
import webbrowser

"""
Twitter API Authentication and Tweet Retrieval.

This program authenticates user credentials with the Twitter API using OAuth 1.0a, 
allowing access to a user's tweets.

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
        "API_KEY": os.getenv("API_KEY"),
        "API_SECRET_KEY": os.getenv("API_SECRET_KEY"),
        "ACCESS_TOKEN": os.getenv("ACCESS_TOKEN"),
        "ACCESS_TOKEN_SECRET": os.getenv("ACCESS_TOKEN_SECRET")
    }
    
def external_user_login() -> tweepy.API:
    """
    Perform OAuth 1.0a user authentication for Twitter API.

    Returns:
        tweepy.API: Authenticated API instance for accessing Twitter API.

    Raises:
        tweepy.TweepyException: If OAuth authentication process encounters errors.
    """
    credentials = load_credentials()
    auth = tweepy.OAuthHandler(credentials["API_KEY"], credentials["API_SECRET_KEY"])

    # Get the authorization URL.
    redirect_url = auth.get_authorization_url()

    # Direct user to the authorization URL.
    print("Please go to this URL and authorize access to your Twitter Account:", redirect_url)
    webbrowser.open(redirect_url)

    # Obtain the verification code from the user.
    verifier = input("Enter the verification code from Twitter:\n")

    # Get the access token.
    try:
        auth.get_access_token(verifier)
        print("Authentication successful!")
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

    # Create the authenticated API object using the authorized handler
    return tweepy.API(auth)

def get_user_tweets(api: tweepy.API, username: str, count: int = 20) -> None:
    """
    Fetch tweets from a specified user using the authenticated API instance.

    :param api: Authenticated API instance for accessing Twitter API.
    :param username: Twitter handle of the user whose tweets are to be fetched.
    :param count: Number of tweets to fetch (default is 20).
    """
    try:
        user = api.get_user(screen_name=username)
        tweets = api.user_timeline(screen_name=username, count=count)
        formatted_tweets = []
        for tweet in tweets:
            formatted_tweet = {
                "text": tweet.text,
            }
            formatted_tweets.append(formatted_tweet)

        with open(f"{username}_tweets.json", "w", encoding="utf-8") as file:
            json.dump(formatted_tweets, file, indent=4)

        print(f"Successfully fetched and stored {len(formatted_tweets)} tweets for {username}.")

    except tweepy.TweepyException as e:
        print(f"Error fetching tweets: {e}")
