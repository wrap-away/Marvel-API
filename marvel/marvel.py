from marvel.base import Base


class Marvel(Base):
    def __init__(self, PUBLIC_KEY, PRIVATE_KEY):
        super().__init__(PUBLIC_KEY, PRIVATE_KEY)
