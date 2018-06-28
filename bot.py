# bot.py

import tweepy
import sqlite3
import datetime

from credentials import *

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)

#Construct the API instance
api = tweepy.API(auth) # create an API object

#DB connection
conn = sqlite3.connect('test.db') # Connect to DB
c = conn.cursor()
# has users table with Name, Date, unique ID, highscore


def user_validate(username):
    name = username
    print(name)
    c.execute("SELECT count(*) FROM users WHERE name = ?", (name,))
    data=c.fetchone()[0]
    if data==0:
        print('There is no user named %s'%name)
        return False
    else:
        print('user %s found in %s row(s)'%(name,data))
        return True

def responder_main(username, status_id, received_msg):
    print("Responding")
    msg = "I am a bot, responding to your tweet."
    n = username

    #Check if user is member:
    is_Mem = user_validate(username)

    if(is_Mem):
        # evaluate message
        msg = '@%s\n You are already signed up!' % (n)
    else:
        # check if they tweeted register, if true, add to DB
        # admin_responder()
        msg = '@%s\n You are not yet signed up! Tweet \"Register\" to join!'  % (n)
    
    api.update_status(msg, status_id)



#create a class inherithing from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name 
        status_id = status.id
        received_msg = status.text

        responder_main(username, status_id, received_msg)


myStreamListener = BotStreamer()

#Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@watt_bot'])


# Add Registration and Start
