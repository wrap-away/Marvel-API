from marvel.modules.base_module import BaseModule


class Series(BaseModule):
    def __init__(self, requester):
        """
        Series Module.
        :param requester: Requester
        """
        super().__init__(requester)

    def all(self, **kwargs):
        """
        This returns data containing all series
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('series', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        """
        This returns data containing a single series using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('series', identifier=identifier, payload=kwargs)
        return data

    def characters(self, identifier, **kwargs):
        """
        This returns data containing a single series's characters using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('series', identifier=identifier, payload=kwargs, sub_endpoint="characters")
        return data

    def comics(self, identifier, **kwargs):
        """
        This returns data containing a single series's comics using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('series', identifier=identifier, payload=kwargs, sub_endpoint="comics")
        return data

    def creators(self, identifier, **kwargs):
        """
        This returns data containing a single series's creators using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('series', identifier=identifier, payload=kwargs, sub_endpoint="creators")
        return data

    def events(self, identifier, **kwargs):
        """
        This returns data containing a single series's events using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('series', identifier=identifier, payload=kwargs, sub_endpoint="events")
        return data

    def stories(self, identifier, **kwargs):
        """
        This returns data containing a single series's stories using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('series', identifier=identifier, payload=kwargs, sub_endpoint="stories")
        return data
