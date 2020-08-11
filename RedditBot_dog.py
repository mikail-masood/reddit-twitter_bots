import praw
import config_dog

def bot_login():
	r = praw.Reddit(username = config_dog.username,
	 		password = config_dog.password,
	 		client_id = config_dog.client_id,
	 		client_secret = config_dog.client_secret,
	 		user_agent = "caramel_mocha dog bot test v.1")
	print("logged in!")

	return r

def run_bot(r):
	print("finding dogs")
	for comment in r.subreddit('test').comments(limit = 25):
		if "dog" in comment.body:
			print ("doggo found")
			comment.reply("doggo doggo woof woof")
			print("replied to comment")

## uncomment the next line for infinite replies!!!!
# while True:
r = bot_login()
run_bot(r)