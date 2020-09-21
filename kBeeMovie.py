import tweepy #Twitter API
import datetime #To calculate line
import urllib.request #Create screen scraper

#Commented out for security
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
bearer_token = ''

#Logs in to twitter via developer keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Puts every line of the script in an array all_lines
script = "https://gist.githubusercontent.com/MattIPv4/045239bc27b16b2bcf7a3a9a4648c08a/raw/2411e31293a35f3e565f61e7490a806d4720ea7e/bee%2520movie%2520script"
file = urllib.request.urlopen(script)
all_lines = file.readlines()

start = datetime.date(2020, 4, 27)
today = datetime.date.today()

#Calculates the exact line to be tweeted based on start date
def getLine():
    num = today - start
    return all_lines[num.days]

#Tweets out line
def publictweet():
    api.update_status(getLine())
    print(getLine())

publictweet()
