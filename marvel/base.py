from marvel.requester import Requester


class Base:
    def __init__(self, PUBLIC_KEY, PRIVATE_KEY, LIMIT):
        """
        Base Class
        :param PUBLIC_KEY: str
        :param PRIVATE_KEY: str
        :param LIMIT: int
        """
        self.requester = Requester(PUBLIC_KEY, PRIVATE_KEY, LIMIT)
