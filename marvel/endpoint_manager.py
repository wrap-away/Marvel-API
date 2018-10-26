class EndpointManager:
    def __init__(self):
        self.base_url = "https://gateway.marvel.com/v1/public"
        self.endpoints = self.get_endpoints()

    def get_endpoints(self):
        endpoints = {
            'characters': self.base_url + '/characters',
            'comics': self.base_url + '/comics',
            'creators': self.base_url + '/creators',
            'events': self.base_url + '/events',
            'series': self.base_url + '/series',
            'stories': self.base_url + '/stories',
        }
        return endpoints

    def get_endpoint(self, name):
        return self.endpoints[name]
