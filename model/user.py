from core.model import BaseModel


class User(BaseModel):
    _TABLE_NAME = "user"
    _KEYS = ("id", "username")

    def __init__(self, **prams):
        super(User, self).__init__(**prams)

    def __str__(self):
        return '%s | %s' % (self.__class__.__name__, self.username)