from datetime import datetime, timedelta
import re

import tweepy as tw


# Twitter API keys
consumer_key = 'INSERT_HERE'
consumer_secret = 'INSERT_HERE'
access_token = 'INSERT_HERE'
access_token_secret = 'INSERT_HERE'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def search_twitter(query, days_ago=10): 
    since=datetime.today() - timedelta(days=days_ago)

    tweets = tw.Cursor(api.search,
                       q=query,
                       lang="en",
                       since=since).items(1000)

    # Remove URLs
    # tweets_no_urls = [remove_url(tweet.text) for tweet in tweets]
    return tweets


def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

