import facebook
import pprint
import urllib3
import json
import tweepy
from datetime import date, timedelta
last_month=date.today() - timedelta(days=30)
import pprint

#estanciar objeto de PI do facebook, se autenticando
token = 'EAARf0KiflmoBAByLWZC9VLmTQt7ZBxEYr0BfZA23gM5PG5kVqi7KOcX5WBB4ifl8gaMmv4N4q5yzcqvEFS2uGaZBBpRV3pLcpfOe0t8bMZCS9ZAPrVZA76NGzyvPabiPin0oA7yYqU3QAfybbQ105ouem58wbOHmrECSbhYrEXTEPKRj3yCO3TkcL6FEE0tBLzZA3FKo7lfJbAZDZD'

graph_api = facebook.GraphAPI(access_token=token,version='3.1')

me = graph_api.get_object('me')

#pprint.pprint(me)#trazer meu usuário

####################################################################

#results = graph_api.request('search', {'q':'games','type':'page'})

#pprint.pprint(results)

my_feed = graph_api.get_connections(me['id'], 'feed')
#pprint.pprint(my_feed)#meus posts

my_likes = graph_api.get_connections(me['id'], 'likes')
#pprint.pprint(my_likes)

CONSUMER_KEY = 'sUotdtsMfNECbiIlESbg1gkOS'
CONSUMER_SECRET = "yXQkSA4DTZ55z3aBKeYKXpK1Aro2C9jNJtzMLagcTaT3RygdpA"

OAUTH_TOKEN = "1795037040-xto2FmaXa84Q0JnjEYiwx4X53cng48WSnnHEKoe"
OAUTH_TOKEN_SECRET = "UftjJDUQJpkPVAqR7wnu0TAkMfKErNWUxqVREfuQEKT2B"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)#autenticador para o usuário
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)


list_likes = []
#correr todas as páginas de retorno, como o sdk traz como http precisa usar o urllib3 e transformar em json data

for i in my_likes:
    list_likes.append(my_likes['data'][0]['name'])

while 'paging' in my_likes.keys() and \
        'next' in my_likes['paging'].keys():

    http = urllib3.PoolManager()
    my_likes = http.request('GET', my_likes['paging']['next'])
    my_likes = json.loads(my_likes.data)#json=javascript object notation
    #names = my_likes.name
    #print(names)

    #pprint.pprint(my_likes['data'][0]['name'])
    list_likes.append(my_likes['data'][0]['name'])
#print(list_likes)

for name in list_likes:
    tweets = tweepy.Cursor(api.search,
                           q=name,
                           since=last_month.strftime('%Y-%m-%d'),
                           until=date.today().strftime('%Y-%m-%d'),
                           include_entities=True,
                           lang='pt').items()
    for t in tweets:
        pprint.pprint(t._json)