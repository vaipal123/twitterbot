import tweepy,time,sys

inputFile = str(sys.argv[1])
CONSUMER_KEY = 'vQ7AWdXJ3qjIsqLHxrXTBYbIe'
CONSUMER_SECRET = 'MOaorEAJknz0mxZP8iDfh4QRGP8VNQUx10gVbthRfYlNS3tw0t'
ACCESS_KEY = '120362878-K1RDF9J6Aew3Lfmbqtj25G6LwAe3y8xu2GIYsMud'
ACCESS_SECRET = 'AZAEXkZGRq93mUAyd3XUdpRdcYRZPEZd9F47UXFWGtZuA'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open(inputFile,'r') as f:
	lines = f.readlines()

for line in lines:
	api.update_status(status = line)
	time.sleep(900)
