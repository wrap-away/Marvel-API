from marvel.modules.base_module import BaseModule


class Events(BaseModule):
    def __init__(self, requester):
        super().__init__(requester)

    def all(self, **kwargs):
        data, headers = self.r.request('events', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs)
        return data

    def characters(self, identifier, **kwargs):
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="characters")
        return data

    def comics(self, identifier, **kwargs):
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="comics")
        return data

    def creators(self, identifier, **kwargs):
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="creators")
        return data

    def series(self, identifier, **kwargs):
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="series")
        return data

    def stories(self, identifier, **kwargs):
        data, headers = self.r.request('events', identifier=identifier, payload=kwargs, sub_endpoint="stories")
        return data
