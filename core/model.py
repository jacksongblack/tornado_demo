from torndb import Connection
import config


class BaseModel(object):
    TABLE_NAME = None
    KEYS = None

    def __init__(self, **fields):
        settings = config.MYSQL_SETTINGS
        self.db = Connection(settings.get('host'), settings.get('database_name'), user=settings.get('username'),
                             password=settings.get("password"))

    def __del__(self):
        self.db.close()

    def get(self, **kwargs):
        refult = ''
        for field_name, field_value in kwargs.items():
            if field_name in self.KEYS:
                sql_tempate = 'SELECT * FROM %s where %s = %s' % (self.TABLE_NAME, field_name, field_value)
                refult = self.db.get(sql_tempate)
        return refult

    def query(self, **kwargs):
        pass
