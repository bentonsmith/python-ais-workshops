# Twitter API:
# https://github.com/bear/python-twitter

import twitter
import pprint

CONSUMER_KEY = 'Ekq990fvqMqekBoy0tskqnIOc'
CONSUMER_SECRET = 'dvhUj7wgc10dxao20sGU2jSeDEUetl2OK5uhx0z7SzZm6xdzlf'
ACCESS_TOKEN = '15837902-oFJomig13kSz3paHZIcgtnhbnGW7jfo3fReXS46t0'
ACCESS_TOKEN_SECRET = 'OB2STskprTCgI5E1knt36cMeUC4of70Olrmy6jVhrum45'

api = twitter.Api(
                consumer_key=CONSUMER_KEY
              , consumer_secret=CONSUMER_SECRET
              , access_token_key=ACCESS_TOKEN
              , access_token_secret=ACCESS_TOKEN_SECRET
              )

users = api.GetFriends()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint([u.screen_name for u in users])