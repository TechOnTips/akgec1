import tweepy
from time import sleep
import os
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

LIKE = True

FOLLOW = False

print("Twitter bot which retweets, like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

for tweet in tweepy.Cursor(api.search, q=('#feeskamkaro OR #AKGEC OR #akgec OR #AKGECfeeskamkaro OR #SpeakUpForStudents -filter:retweets'), lang='en').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        if LIKE:
            tweet.favorite()
            print('Favorited the tweet')

        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')

        sleep(61)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
