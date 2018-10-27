from marvel.modules.base_module import BaseModule


class Events(BaseModule):
    def __init__(self, requester):
        """
        Events Module.
        :param requester: Requester
        """
        super().__init__(requester)

    def all(self, **kwargs):
        """
        This returns data containing all events
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('events', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        """
        This returns data containing a single event using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs)
        return data

    def characters(self, identifier, **kwargs):
        """
        This returns data containing a single event's characters using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="characters")
        return data

    def comics(self, identifier, **kwargs):
        """
        This returns data containing a single event's comics using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="comics")
        return data

    def creators(self, identifier, **kwargs):
        """
        This returns data containing a single event's creators using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="creators")
        return data

    def series(self, identifier, **kwargs):
        """
        This returns data containing a single event's series using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="series")
        return data

    def stories(self, identifier, **kwargs):
        """
        This returns data containing a single event's stories using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="stories")
        return data
