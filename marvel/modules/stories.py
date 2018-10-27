from marvel.modules.base_module import BaseModule


class Stories(BaseModule):
    def __init__(self, requester):
        """
        Stories Module.
        :param requester: Requester
        """
        super().__init__(requester)

    def all(self, **kwargs):
        """
        This returns data containing all stories
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('stories', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        """
        This returns data containing a single story using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs)
        return data

    def characters(self, identifier, **kwargs):
        """
        This returns data containing a single story's characters using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs, sub_endpoint="characters")
        return data

    def comics(self, identifier, **kwargs):
        """
        This returns data containing a single story's comics using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.requester('stories', identifier=identifier, payload=kwargs, sub_endpoint='comics')
        return data

    def creators(self, identifier, **kwargs):
        """
        This returns data containing a single story's creators using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs, sub_endpoint="creators")
        return data

    def events(self, identifier, **kwargs):
        """
        This returns data containing a single story's events using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs, sub_endpoint="events")
        return data

    def series(self, identifier, **kwargs):
        """
        This returns data containing a single story's series using identifier (id)
        :param identifier: int
        :param kwargs: dict
        :return: dict
        """
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs, sub_endpoint="series")
        return data
