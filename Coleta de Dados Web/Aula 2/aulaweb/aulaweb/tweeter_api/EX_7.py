import tweepy
import pprint

CONSUMER_KEY = 'sUotdtsMfNECbiIlESbg1gkOS'
CONSUMER_SECRET = "yXQkSA4DTZ55z3aBKeYKXpK1Aro2C9jNJtzMLagcTaT3RygdpA"

OAUTH_TOKEN = "1795037040-xto2FmaXa84Q0JnjEYiwx4X53cng48WSnnHEKoe"
OAUTH_TOKEN_SECRET = "UftjJDUQJpkPVAqR7wnu0TAkMfKErNWUxqVREfuQEKT2B"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)#autenticador para o usuário
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)


world_trends = api.trends_place(455827)#SP capital
#pprint.pprint(world_trends[0]['trends'])

list_trends = []
for t in world_trends[0]['trends']:
    list_trends.append(t['name'])

#print(list_trends)

class MyStreamListener(tweepy.StreamListener):#herda de StreamListener
    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth,
                         listener=myStreamListener)

myStream.filter(track=list_trends,
                is_async=True)


