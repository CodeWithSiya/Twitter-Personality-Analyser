import tweepy
from dotenv import load_dotenv
import os

"""
Program which authenticates the required credentials from the Twitter API and retrieve the tweets from the specified username.
:author: Siyabonga Madondo
:version: 15/07/2024
"""

client = None

def configure() -> None:
    """
    Load the configuration keys from the dotenv file.
    :return: None
    """
    load_dotenv()

def authenticate() -> None:
    """
    Authenticate details with the Twitter API.
    :return: None
    """
    global client
    client = tweepy.Client(
        bearer_token = os.getenv("bearer_token"),
        consumer_key = os.getenv("api_key"),
        consumer_secret = os.getenv("api_secret_key"),
        access_token = os.getenv("access_token"),
        access_token_secret = os.getenv("access_token_secret")
    )

def verify_authentication() -> None:
    """
    Verify if the authentication is successful by fetching user details.
    :return: None
    """
    try:
        user = client.get_me()
        print(f"Authentication successful! Authenticated as: {user.data.username}")
    except tweepy.TweepyException as e:
        print(f"Authentication failed: {e}")

# def get_tweets(username: str, count: int = 5) -> list:
#     """
#     Get the tweets from the specified user name.
#     :param username: The username to fetch tweets from.
#     :param count: The number of tweets to fetch.
#     :return: List of tweet texts.
#     """
#     user = client.get_user(username=username)
#     tweets = client.get_users_tweets(id=user.data.id, max_results=count, tweet_fields=["text"])
#     tweet_texts = [tweet.text for tweet in tweets.data]
#     return tweet_texts

def main():
    configure()
    authenticate()
    verify_authentication()
    #tweets = get_tweets(os.getenv('user_name'), 1)
    #for tweet in tweets:
    #    print(tweet)

if __name__ == "__main__":
    """
    Authenticate the required credentials from the Twitter API and retrieve the tweets from the specified username.
    """
    main()