##########################
# Requests for REST APIs #
##########################
'''
http://docs.python-requests.org/en/latest/

Requests is an http client for Python available from
http://docs.python-requests.org/en/latest/user/install/#install


Install with pip (pip install requests)
'''
API_KEY = '0kj_v4k3n1oTBWL_A5MkckOv_CW9l7xg'
import requests

# You could insert any http resource here! Amazing
r = requests.get(f'http://api.mongolab.com/api/1/databases/mis/collections/book_collection?apiKey={API_KEY}')

print('Status',r.status_code) # Should be 200 et. al.

r.json()

# query
r = requests.get(f'http://api.mongolab.com/api/1/databases/mis/collections/book_collection?q={{"tags": "rabbit"}}&apiKey={API_KEY}')

# Pretty Print
import pprint
printer = pprint.PrettyPrinter(indent=4)
printer.pprint(r.json())


