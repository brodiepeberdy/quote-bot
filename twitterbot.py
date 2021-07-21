import twitter
import requests


def auth():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
    try:
        api = twitter.Api(consumer_key, consumer_secret, access_token, access_secret)
        print ("LOGGED INTO TWITTER.")
        return api
    except Exception as e:
        print (e + "TWITTER LOGIN FAILED.")

def tweet(api, message):
    try:
        status = api.PostUpdate(message)
        print ("Tweet posted.")
    except Exception as e:
        print (str(e) + "FAILED TO TWEET")

api = auth()
response = requests.get("https://zenquotes.io/api/random")
quote = str(response.json()[0]['q']) + " - " + str(response.json()[0]['a'])
print(quote)
tweet(api, quote)
