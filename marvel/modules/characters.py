from marvel.modules.base_module import BaseModule


class Characters(BaseModule):
    def __init__(self, requester):
        """
        Characters Module.
        :param requester: Requester
        """
        super().__init__(requester)

    def all(self, **kwargs):
        """
        This returns data containing all characters
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('characters', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        """
        This returns data containing a single character using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('characters', identifier=identifier, payload=kwargs)
        return data

    def comics(self, identifier, **kwargs):
        """
        This returns data containing a single character's comics using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('characters', identifier=identifier, payload=kwargs, sub_endpoint="comics")
        return data

    def events(self, identifier, **kwargs):
        """
        This returns data containing a single character's events using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('characters', identifier=identifier, payload=kwargs, sub_endpoint="events")
        return data

    def series(self, identifier, **kwargs):
        """
        This returns data containing a single character's series using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('characters', identifier=identifier, payload=kwargs, sub_endpoint="series")
        return data

    def stories(self, identifier, **kwargs):
        """
        This returns data containing a single character's stories using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('characters', identifier=identifier, payload=kwargs, sub_endpoint="stories")
        return data
