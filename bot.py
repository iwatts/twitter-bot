# bot.py

import tweepy
import sqlite3
from credentials import *

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)

#Construct the API instance
api = tweepy.API(auth) # create an API object

conn = sqlite3.connect('test.db') # Connect to DB
c = conn.cursor()

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

def user_validate(username):
    c.execute("SELECT count(*) FROM components WHERE name = ?", (username))
    data=c.fetchone()[0]
    if data==0:
        print('There is no user named %s'%name)
        return false
    else:
        print('user %s found in %s row(s)'%(name,data))
        return true

def responder_agb(username, status_id, received_msg):
    print("Responding")
    msg = "I am a bot, responding to your tweet."

    #Check if user is member:
	#	update msg
    #	msg = game_listener(received_msg)
    #else:
    #	msg = admin_listener()
    is_Mem = user_validate(username)

    if(!is_Mem):
        # check if they tweeted register, if true, add to DB
        msg = "You are not yet signed up! Tweet \"Register\" to join!"
    else:
        msg = "You are already signed up!"
    
    api.update_status(msg, status_id)



#create a class inherithing from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name 
        status_id = status.id
        received_msg = status.full_text

        responder_agb(username, status_id, received_msg)


myStreamListener = BotStreamer()

#Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@The_Icean'], tweet_mode='extended')


# Add Registration and Start
