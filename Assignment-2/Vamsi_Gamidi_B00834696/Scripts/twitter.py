import tweepy
import re
import json
import datetime


def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())


def dateTimeConverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


consumer_key = "uUVXPL7uNJ1cIKaFTzt75I1He"
consumer_secret = "JGVJByOXksZdzlnJEUosevcXIawzVyp5jFYZIs8Jps8tDfeq8h"
access_token = "3258767688-WmDNUA6grXmdnE1BxwfVHjpmB36tGQepmuJYv9B"
access_token_secret = "4ibzXIDQ5W9neqSEq9tMuaNTNFSqZKKxBOEq2zj5WFEfa"

authorization = tweepy.OAuthHandler(consumer_key, consumer_secret)
authorization.set_access_token(access_token, access_token_secret)
api = tweepy.API(authorization, wait_on_rate_limit=True)

tweets_on_canada = []
tweets_on_univ = []
tweets_on_dal = []
tweets_on_halifax = []
tweets_on_canada_education = []

search_word = "Canada"
tweets_on_canada = tweepy.Cursor(api.search,
                                 q=search_word,
                                 lang="en",
                                 tweet_mode="extended").items(650)

search_word = "University"
tweets_on_univ = tweepy.Cursor(api.search,
                               q=search_word,
                               lang="en",
                               tweet_mode="extended").items(650)

search_word = "Dalhousie University"
tweets_on_dal = tweepy.Cursor(api.search,
                              q=search_word,
                              lang="en",
                              tweet_mode="extended").items(650)

search_word = "Halifax"
tweets_on_halifax = tweepy.Cursor(api.search,
                                  q=search_word,
                                  lang="en",
                                  tweet_mode="extended").items(650)

search_word = "Canada Education"
tweets_on_canada_education = tweepy.Cursor(api.search,
                                           q=search_word,
                                           lang="en",
                                           tweet_mode="extended").items(650)
tweets_on_canada_text = []
data = []

for tweet in tweets_on_canada:
    try:
        text = tweet.retweeted_status.full_text = "RT " + remove_url(tweet.retweeted_status.full_text)
        tweets_on_canada_text.append(tweet.retweeted_status.full_text)

    except AttributeError:
        text = tweet.full_text = remove_url(tweet.full_text)
        tweets_on_canada_text.append(tweet.full_text)

    if tweet.user.location == "":
        tweet.user.location = "Nan"

    tweets_on_canada_text.append(tweet.user.location)
    data.append({
        'Tweet_Text': text,
        'Location': tweet.user.location,
        'Date': tweet.created_at
    })
for tweet in tweets_on_dal:
    try:
        text = tweet.retweeted_status.full_text = "RT " + remove_url(tweet.retweeted_status.full_text)
        tweets_on_canada_text.append(tweet.retweeted_status.full_text)

    except AttributeError:
        text = tweet.full_text = remove_url(tweet.full_text)
        tweets_on_canada_text.append(tweet.full_text)

    if tweet.user.location == "":
        tweet.user.location = "Nan"

    tweets_on_canada_text.append(tweet.user.location)
    data.append({
        'Tweet_Text': text,
        'Location': tweet.user.location,
        'Date': tweet.created_at
    })

for tweet in tweets_on_canada_education:
    try:
        text = tweet.retweeted_status.full_text = "RT " + remove_url(tweet.retweeted_status.full_text)
        tweets_on_canada_text.append(tweet.retweeted_status.full_text)

    except AttributeError:
        text = tweet.full_text = remove_url(tweet.full_text)
        tweets_on_canada_text.append(tweet.full_text)

    if tweet.user.location == "":
        tweet.user.location = "Nan"

    tweets_on_canada_text.append(tweet.user.location)
    data.append({
        'Tweet_Text': text,
        'Location': tweet.user.location,
        'Date': tweet.created_at
    })

for tweet in tweets_on_univ:
    try:
        text = tweet.retweeted_status.full_text = "RT " + remove_url(tweet.retweeted_status.full_text)
        tweets_on_canada_text.append(tweet.retweeted_status.full_text)

    except AttributeError:
        text = tweet.full_text = remove_url(tweet.full_text)
        tweets_on_canada_text.append(tweet.full_text)

    if tweet.user.location == "":
        tweet.user.location = "Nan"

    tweets_on_canada_text.append(tweet.user.location)
    data.append({
        'Tweet_Text': text,
        'Location': tweet.user.location,
        'Date': tweet.created_at
    })

for tweet in tweets_on_halifax:
    try:
        text = tweet.retweeted_status.full_text = "RT " + remove_url(tweet.retweeted_status.full_text)
        tweets_on_canada_text.append(tweet.retweeted_status.full_text)

    except AttributeError:
        text = tweet.full_text = remove_url(tweet.full_text)
        tweets_on_canada_text.append(tweet.full_text)

    if tweet.user.location == "":
        tweet.user.location = "Nan"

    tweets_on_canada_text.append(tweet.user.location)
    data.append({
        'Tweet_Text': text,
        'Location': tweet.user.location,
        'Date': tweet.created_at
    })

with open('tweets.json', 'w') as outfile:
    json.dump(data, outfile, default=dateTimeConverter)
