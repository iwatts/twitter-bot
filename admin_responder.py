# admin_responder.py

register(username):
	regTime = datetime.datetime.now().time()
	c.execute("INSERT INTO users VALUES ('%s', '%s', null, 0)" % / (username, regTime))
	c.commit()
	c.close()
	
# delete()
# show_high_score()
# start()