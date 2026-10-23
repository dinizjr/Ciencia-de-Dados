import facebook
import pprint
import urllib3
import json

#estanciar objeto de PI do facebook, se autenticando
token = 'EAARf0KiflmoBAByLWZC9VLmTQt7ZBxEYr0BfZA23gM5PG5kVqi7KOcX5WBB4ifl8gaMmv4N4q5yzcqvEFS2uGaZBBpRV3pLcpfOe0t8bMZCS9ZAPrVZA76NGzyvPabiPin0oA7yYqU3QAfybbQ105ouem58wbOHmrECSbhYrEXTEPKRj3yCO3TkcL6FEE0tBLzZA3FKo7lfJbAZDZD'

graph_api = facebook.GraphAPI(access_token=token,version='3.1')

me = graph_api.get_object('me')

pprint.pprint(me)#trazer meu usuário

####################################################################

#results = graph_api.request('search', {'q':'games','type':'page'})

#pprint.pprint(results)

my_feed = graph_api.get_connections(me['id'], 'feed')
pprint.pprint(my_feed)#meus posts

my_likes = graph_api.get_connections(me['id'], 'likes')
pprint.pprint(my_likes)

#correr todas as páginas de retorno, como o sdk traz como http precisa usar o urllib3 e transformar em json data
while 'paging' in my_likes.keys() and \
        'next' in my_likes['paging'].keys():

    http = urllib3.PoolManager()
    my_likes = http.request('GET', my_likes['paging']['next'])
    my_likes = json.loads(my_likes.data)#json=javascript object notation
    pprint.pprint(my_likes)