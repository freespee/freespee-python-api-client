from freespee_api import Freespee

api = Freespee('tag', 'password')
response = api.get('customers')

print response.result