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
        if sub_endpoint is not None:
            url += "/" + str(identifier) + "/" + sub_endpoint
        query = self.get_query_with_authentication_params(payload)
        self.r = requests.get(url, params=query)
        if raw:
            return self.r
        self.check_for_exceptions(self.r)
        return self.r.json(), self.r.headers

    def get_query_with_authentication_params(self, payload):
        timestamp = int(time())
        input_string = str(timestamp) + self.PUBLIC_KEY + self.PRIVATE_KEY
        hash = md5(input_string.encode("utf-8")).hexdigest()
        payload['ts'] = timestamp
        payload['apikey'] = self.PUBLIC_KEY
        payload['hash'] = hash
        return payload

    @staticmethod
    def check_for_exceptions(request):
        status_code = request.status_code
        if status_code == 200:
            return
        elif status_code == 400:
            raise InvalidInputException("Invalid input")
        elif status_code == 404:
            raise NotFoundException("Not Found")
        elif status_code == 403:
            raise InvalidAPIKEYException("Invalid API KEY")
        else:
            raise ConnectionErrorException("The website couldn't be retrieved.")
