import requests
from hashlib import md5
from time import time
from marvel.exceptions import *
from marvel.endpoint_manager import EndpointManager


class Requester(EndpointManager):
    def __init__(self, PUBLIC_KEY, PRIVATE_KEY, LIMIT):
        """
        Requester class responsible for making HTTP requests.
        :param PUBLIC_KEY: str
        :param PRIVATE_KEY: str
        """
        super().__init__()
        self.PUBLIC_KEY = PUBLIC_KEY
        self.PRIVATE_KEY = PRIVATE_KEY
        self.r = object
        self.limit = LIMIT

    def request(self, endpoint_name, payload=None, sub_endpoint=None, identifier=None, raw=None):
        """
        Request a route with data.
        :param endpoint_name: str
        :param payload: dict
        :param sub_endpoint: str
        :param identifier: int
        :param raw: bool
        :return: dict, dict
        """
        if payload is None:
            payload = {}
        url = self.endpoints[endpoint_name]
        if identifier is not None:
            url += "/" + str(identifier)
        if sub_endpoint is not None:
            url += "/" + sub_endpoint
        if self.limit is not None:
            assert self.limit <= 100, (
                    "limit %d higher than the maximum 100 can be supported" % self.limit
            )
            payload["limit"] = self.limit
        query = self.get_query_with_authentication_params(payload)
        self.r = requests.get(url, params=query)
        if raw:
            return self.r
        json_data = self.r.json()
        self.check_for_exceptions(self.r, json_data)
        return json_data, self.r.headers

    def get_query_with_authentication_params(self, payload):
        """
        Authenticate a request.
        :param payload: dict
        :return: dict
        """
        timestamp = int(time())
        input_string = str(timestamp) + self.PRIVATE_KEY + self.PUBLIC_KEY
        hash = md5(input_string.encode("utf-8")).hexdigest()
        payload['ts'] = timestamp
        payload['apikey'] = self.PUBLIC_KEY
        payload['hash'] = hash
        return payload

    @staticmethod
    def check_for_exceptions(request, json_data):
        """
        Raises exception for errors.
        :param request: Request
        :param json_data: dict
        :return: None
        """
        status_code = request.status_code
        if status_code == 200:
            return
        elif 'code' in json_data:
            if'status' in json_data:
                error_message = "{} {}".format(str(json_data['code']), json_data['status'])
                raise MarvelException(error_message)
            elif 'message' in json_data:
                error_message = "{} {}".format(str(json_data['code']), json_data['message'])
                raise MarvelException(error_message)
            else:
                error_message = "Something went horribly wrong. {}".format(json_data)
                raise BadInputException(error_message)
        else:
            error_message = "Something went horribly wrong. {}".format(json_data)
            raise BadInputException(error_message)
