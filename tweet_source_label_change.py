#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='consumer key',
consumer_secret='secret key',
access_token='access token', 
access_token_secret='secter access token'
)

user = "username"

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def tweet():
	message=input("tweet: ")
	api.update_status('twitter for watermelon')
	time.sleep(1000)
if __name__ == "__main__":
			while 1:
				tweet()
