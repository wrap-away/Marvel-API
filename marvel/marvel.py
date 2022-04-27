from marvel.base import Base
from marvel.modules.characters import Characters
from marvel.modules.events import Events
from marvel.modules.series import Series
from marvel.modules.comics import Comics
from marvel.modules.creators import Creators
from marvel.modules.stories import Stories


class Marvel(Base):
    def __init__(self, PUBLIC_KEY, PRIVATE_KEY, LIMIT=None):
        """
        Marvel main class to access different modules and their methods.
        :param PUBLIC_KEY: str
        :param PRIVATE_KEY: str
        :param LIMIT: int
        """
        super().__init__(PUBLIC_KEY, PRIVATE_KEY, LIMIT)
        self.characters = Characters(requester=self.requester)
        self.events = Events(requester=self.requester)
        self.series = Series(requester=self.requester)
        self.comics = Comics(requester=self.requester)
        self.creators = Creators(requester=self.requester)
        self.stories = Stories(requester=self.requester)