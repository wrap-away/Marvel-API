from marvel.base import Base
from marvel.modules.characters import Characters


class Marvel(Base):
    def __init__(self, PUBLIC_KEY, PRIVATE_KEY):
        super().__init__(PUBLIC_KEY, PRIVATE_KEY)
        self.characters = Characters(requester=self.requester)
