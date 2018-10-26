from marvel.base import Base
from marvel.modules.characters import Characters
from marvel.modules.events import Events
from marvel.modules.series import Series


class Marvel(Base):
    def __init__(self, PUBLIC_KEY, PRIVATE_KEY):
        super().__init__(PUBLIC_KEY, PRIVATE_KEY)
        self.characters = Characters(requester=self.requester)
        self.events = Events(requester=self.requester)
        self.series = Series(requester=self.requester)

