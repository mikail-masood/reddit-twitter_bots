import(praw)
import(config_bot_v1)

def bot_login():
	x = praw.Reddit(username = config_bot_v1.username,
	 		password = config_bot_v1.password,
	 		client_id = config_bot_v1.client_id,
	 		client_secret = config_bot_v1.client_secret,
	 		user_agent = "U of T Helper Bot v1.1")
	#print("logged in!")

	return x
def run_bot(x):
	for comment in x.subreddit('test').comments(limit = 50):
		if "?" in comment.body:
			#print ("doggo found")
			comment.reply("May I be of assisstance... ")
			#print("replied to comment")


while True:
	x = bot_login
	run_bot(x)
