from marvel.modules.base_module import BaseModule


class Characters(BaseModule):
    def __init__(self, requester):
        super().__init__(requester)

    def all(self):
        data, headers = self.r.request('categories')
        return data

    def get(self, **kwargs):
        data, headers = self.r.request('categories', payload=locals())
        return data

    def comics(self, **kwargs):
        data, headers = self.r.request('categories', payload=locals(), sub_endpoint="comics")
        return data

    def events(self, **kwargs):
        data, headers = self.r.request('categories', payload=locals(), sub_endpoint="events")
        return data

    def series(self, **kwargs):
        data, headers = self.r.request('categories', payload=locals(), sub_endpoint="series")
        return data

    def stories(self, **kwargs):
        data, headers = self.r.request('categories', payload=locals(), sub_endpoint="stories")
        return data
