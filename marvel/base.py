from marvel.requester import Requester


class Base:
    def __init__(self, API_KEY):
        self.requester = Requester(API_KEY)
