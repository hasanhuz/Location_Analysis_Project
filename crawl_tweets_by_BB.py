#!/usr/local/bin/python
# -*- coding: utf-8 -*-

Author = 'Hassan'
Date = 'Jan 2018'

# Modified by Caleigh in Jan 2018

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from time import sleep

#Twitter API keys

consumer_key= 
consumer_secret= 
access_token=
access_secret=

# This is a basic listener that just prints received tweets to stdout.
import tweepy

# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        """This function helps to extract data from Twitter streaming API

        Data output format: json object"""
        data = status
        with open(sys.argv[1], 'a') as f:
            #print data
            print >> f, json.dumps(data._json, ensure_ascii=False).encode('utf-8')
        
    def on_error(self, status_code):
        "Error handlers when streaming is disconnected"
        if status_code == 420:
            return False


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    myStreamListener = MyStreamListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)


    myStream = tweepy.Stream(auth, myStreamListener)
    #This line filter Twitter Streams to capture data by the keywords as specified in words list!
    while True:
        try:
            print('...start crawling...')
            myStream.filter(track='41.82046,-141.50390,77.63183,-52.55859')
                  
        except tweepy.TweepError as e:
            print("some error : " + str(e))
            print("retrying in 20 seconds")
            time.sleep(20)
            continue
    
