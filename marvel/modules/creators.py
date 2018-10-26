from marvel.modules.base_module import BaseModule


class Creators(BaseModule):
    def __init__(self, requester):
        super().__init__(requester)

    def all(self, **kwargs):
        data, headers = self.r.request('creators', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs)
        return data

    def comics(self, identifier, **kwargs):
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs, sub_endpoint="comics")
        return data

    def events(self, identifier, **kwargs):
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs, sub_endpoint="events")
        return data

    def series(self, identifier, **kwargs):
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs, sub_endpoint="series")
        return data

    def stories(self, identifier, **kwargs):
        data, headers = self.r.request('creators', identifier=identifier, payload=kwargs, sub_endpoint="stories")
        return data
