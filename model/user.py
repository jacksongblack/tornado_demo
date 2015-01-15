from core.model import BaseModel


class User(BaseModel):
    TABLE_NAME = "user"
    KEYS = ("id", "username")

    def __init__(self, **prams):
        super(User, self).__init__(**prams)