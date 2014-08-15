import base64
from freespee_api import Freespee

api = Freespee('tag', 'password')

print 'Fetching customers...'

response = api.get('customers')

customers = {}

for customer in response.result['customers']:
    customers[customer['name']] = customer['customer_id']
    print customer['name']

customer_name = raw_input('Choose a customer: ')

print 'Fetching recordings...'

response = api.get('recordings?customer_id=' + customers[customer_name])

for recording in response.result['recordings']:
    print recording['recording_id']

recording_id = raw_input('Choose a recording ID: ')

print 'Downloading recording...'

response = api.get('recordings?recording_id=' + recording_id)

filepath = '/tmp/' + recording_id + '.mp3'

file = open(filepath, 'w')
file.write(base64.b64decode(response.result['recordings'][0]['sounddata']))
file.close

print 'Done! Recording saved as ' + filepath