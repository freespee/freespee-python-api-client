import requests
from requests.auth import HTTPDigestAuth

LATEST_VERSION = '2.4.9'
BASE_URL = 'https://api.analytics.freespee.com/' + LATEST_VERSION

class Freespee:
    result = None

    def __init__(self, username, password, base_url = None):
        self.username = username
        self.password = password
        self.base_url = base_url or BASE_URL

    def set_base_url(self, url):
        self.base_url = url
        
    def make_request(self, method, resource, payload = None):
        args = {'auth': HTTPDigestAuth(self.username, self.password)}

        if (payload):
            args['data'] = payload

        self.result = getattr(requests, method)(self.base_url + '/' + resource, **args)

        response = ApiResponse()
        response.httpCode = self.result.status_code
        response.result = self.result.json()
        return response

    def get(self, resource):
        return self.make_request('get', resource)

    def post(self, resource, data):
        return self.make_request('post', resource, data)

    def put(self, resource, data):
        return self.make_request('put', resource, data)

    def delete(self, resource):
        return self.make_request('delete', resource)

class ApiResponse:
    httpCode = None
    result = None

    def __init__(self):
        pass