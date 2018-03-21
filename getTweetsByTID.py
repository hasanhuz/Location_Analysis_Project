#!/usr/bin/env python
# encoding: utf-8

author = "Hassan"
date="May 3, 2017"

import csv
import json
import tweepy
import time
import re

#from keys import keys #keep keys in separate file, keys.py
consumer_key= 
consumer_secret= 
access_token= 
access_secret= 

#API authenication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


def getTweetsByIds(tweet_id):
    """take a user_id as input and return the number of tweets for that user

    str -> str"""
    try:
        tweet = api.get_status(tweet_id)
        tweet= (tweet.text).encode('utf-8')
        tweet= re.sub('\s+', ' ', tweet)
        return tweet_id, tweet.strip()
    
    except tweepy.TweepError as e:
        # Just exit if any error
        print("some error : " + str(e))
        print("retrying in 20 seconds")
        time.sleep(1)
        continue

def write_tweet_to_file(filename, tweet_id, tweet):
    """save given data input into an output file"

    str, str, str -> None"""
    out_p=open(filename, 'ab') 
    writer = csv.writer(out_p,delimiter = ',', quoting=csv.QUOTE_ALL)
    writer.writerow(('tweet_id','tweet'))
    writer.writerow((tweet_id,tweet))
    out_p.flush()
    
tweet_id, tweet= getTweetsByIds(tweet_id)
write_tweet_to_file(filename, tweet_id, tweet)    
