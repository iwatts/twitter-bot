# bot.py

import tweepy
from credentials import *

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_token_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

def responed_adv(username, status_id):
    print("Responding")
    msg = "I am a bot, responding to your tweet."
    api.update_status(msg, status_id)



#create a class inherithing from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name 
        status_id = status.id

        responed_adv(username, status_id)


myStreamListener = BotStreamer()

#Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)

stream.filter(track=['@The_Icean'])


# Add Registration and Start
# Evaluate user messages
# Return Message depending on user input
