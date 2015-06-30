
class Map(dict):
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.__dict__ = self
