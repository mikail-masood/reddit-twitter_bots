#!/usr/bin/env python
import sys, os, time
import tweepy
keys = dict(
consumer_key='abXoIUXZjAdJ7HKKu83mcBJr3',
consumer_secret='OnfSwyjkCASzhQfsJ9ZdV5CZVFsXDqe6eTVs2o31WTaGEa1WWt',
access_token='824714493863297024-Hg2o0cqgMaKGWWdn702KjJHHZe9CyWM', 
access_token_secret='E8fm2SbSNtguXmPqK5EnvG72Mu9ihrsSUqReYtFPLIMpJ'
)

user = "@MikailMasood"

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