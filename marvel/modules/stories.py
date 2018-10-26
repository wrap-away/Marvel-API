from marvel.modules.base_module import BaseModule


class Stories(BaseModule):
    def __init__(self, requester):
        super().__init__(requester)

    def all(self, **kwargs):
        data, headers = self.r.request('stories', payload=kwargs)
        return data

    def get(self, identifier, **kwargs):
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs)
        return data

    def characters(self, identifier, **kwargs):
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs, sub_endpoint="characters")
        return data

    def comics(self, identifier, **kwargs):
        data, headers = self.r.requester('stories', identifier=identifier, payload=kwargs, sub_endpoint='comics')
        return data

    def creators(self, identifier, **kwargs):
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs, sub_endpoint="creators")
        return data

    def events(self, identifier, **kwargs):
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs, sub_endpoint="events")
        return data

    def series(self, identifier, **kwargs):
        data, headers = self.r.request('stories', identifier=identifier, payload=kwargs, sub_endpoint="series")
        return data
