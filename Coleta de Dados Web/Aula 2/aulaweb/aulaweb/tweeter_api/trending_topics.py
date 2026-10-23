import tweepy
import pprint

CONSUMER_KEY = 'sUotdtsMfNECbiIlESbg1gkOS'
CONSUMER_SECRET = "yXQkSA4DTZ55z3aBKeYKXpK1Aro2C9jNJtzMLagcTaT3RygdpA"

OAUTH_TOKEN = "1795037040-xto2FmaXa84Q0JnjEYiwx4X53cng48WSnnHEKoe"
OAUTH_TOKEN_SECRET = "UftjJDUQJpkPVAqR7wnu0TAkMfKErNWUxqVREfuQEKT2B"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)#autenticador para o usuário
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

#WOEID #http://woeid.rosselliot.co.nz/lookup/

#world_trends = api.trends_place(1)#1 é mundial
#pprint.pprint(world_trends)

#world_trends = api.trends_place(23424768)#Brasil
#pprint.pprint(world_trends)


#world_trends = api.trends_place(455913)#Sorocaba
#pprint.pprint(world_trends)

world_trends = api.trends_place(455827)#SP
pprint.pprint(world_trends)