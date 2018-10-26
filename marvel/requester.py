import requests
from hashlib import md5
from time import time
from marvel.exceptions import *
from marvel.endpoint_manager import EndpointManager


class Requester(EndpointManager):
    def __init__(self, PUBLIC_KEY, PRIVATE_KEY):
        super().__init__()
        self.PUBLIC_KEY = PUBLIC_KEY
        self.PRIVATE_KEY = PRIVATE_KEY
        self.r = object

    def request(self, endpoint_name, payload=None, sub_endpoint=None, identifier=None, raw=None):
        if payload is None:
            payload = {}
        url = self.endpoints[endpoint_name]
        if identifier is not None:
            url += "/" + str(identifier)
        if sub_endpoint is not None:
            url += "/" + sub_endpoint
        query = self.get_query_with_authentication_params(payload)
        self.r = requests.get(url, params=query)
        if raw:
            return self.r
        json_data = self.r.json()
        self.check_for_exceptions(self.r, json_data)
        return json_data, self.r.headers

    def get_query_with_authentication_params(self, payload):
        timestamp = int(time())
        input_string = str(timestamp) + self.PRIVATE_KEY + self.PUBLIC_KEY
        hash = md5(input_string.encode("utf-8")).hexdigest()
        payload['ts'] = timestamp
        payload['apikey'] = self.PUBLIC_KEY
        payload['hash'] = hash
        return payload

    @staticmethod
    def check_for_exceptions(request, json_data):
        status_code = request.status_code
        if status_code == 200:
            return
        elif 'code' in json_data and 'message' in json_data:
            raise MarvelException(json_data['code'] + json_data['message'])
        else:
            raise BadInputException("Something went horribly wrong.")
