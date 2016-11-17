import tweepy,time,sys

inputFile = str(sys.argv[1])
CONSUMER_KEY = 'KeyHere'
CONSUMER_SECRET = 'SecretHere'
ACCESS_KEY = 'AccessKeyhere'
ACCESS_SECRET = 'accessSecretHere'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open(inputFile,'r') as f:
	lines = f.readlines()

for line in lines:
	api.update_status(status = line)
	time.sleep(900)
