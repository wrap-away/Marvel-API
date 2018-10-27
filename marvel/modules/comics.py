from marvel.modules.base_module import BaseModule


class Comics(BaseModule):
    def __init__(self, requester):
        """
        Series Module.
        :param requester: Requester
        """
        super().__init__(requester)

    def all(self, **kwargs):
        """
        This returns data containing all ccmics
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('comics', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        """
        This returns data containing a single comic using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('comics', identifier=identifier, payload=kwargs)
        return data

    def characters(self, identifier, **kwargs):
        """
        This returns data containing a single comic's characters using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('comics', identifier=identifier, payload=kwargs, sub_endpoint="characters")
        return data

    def creators(self, identifier, **kwargs):
        """
        This returns data containing a single comic's creators using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('comics', identifier=identifier, payload=kwargs, sub_endpoint="creators")
        return data

    def events(self, identifier, **kwargs):
        """
        This returns data containing a single comic's events using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('comics', identifier=identifier, payload=kwargs, sub_endpoint="events")
        return data

    def stories(self, identifier, **kwargs):
        """
        This returns data containing a single comic's stories using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('comics', identifier=identifier, payload=kwargs, sub_endpoint="stories")
        return data
