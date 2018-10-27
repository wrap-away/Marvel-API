from marvel.modules.base_module import BaseModule


class Creators(BaseModule):
    def __init__(self, requester):
        """
        Creators Module.
        :param requester: Requester
        """
        super().__init__(requester)

    def all(self, **kwargs):
        """
        This returns data containing all creators
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('creators', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        """
        This returns data containing a single creator using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs)
        return data

    def comics(self, identifier, **kwargs):
        """
        This returns data containing a single creator's comics using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs, sub_endpoint="comics")
        return data

    def events(self, identifier, **kwargs):
        """
        This returns data containing a single creator's events using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs, sub_endpoint="events")
        return data

    def series(self, identifier, **kwargs):
        """
        This returns data containing a single creator's series using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs, sub_endpoint="series")
        return data

    def stories(self, identifier, **kwargs):
        """
        This returns data containing a single creator's stories using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs, sub_endpoint="stories")
        return data
