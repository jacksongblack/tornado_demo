from torndb import Connection
import config


class BaseModel(object):
    TABLE_NAME = None
    KEYS = None

    def __init__(self, **fields):
        settings = config.MYSQL_SETTINGS
        self.host = settings.get('host')
        self.database_name = settings.get('database_name')
        self.user = settings.get('username')
        self.password = settings.get('password')

    def __del__(self):
        self.db.close()

    def connection(self):
        self.db = Connection(self.host, self.database_name, user=self.user, password=self.password)
        return self.db

    def close(self):
        self.db.close()

    def get(self, **kwargs):
        result = ''
        for field_name, field_value in kwargs.items():
            if field_name in self.KEYS:
                sql_tempate = 'SELECT * FROM %s where %s = %s' % (self.TABLE_NAME, field_name, field_value)
                result = self.connection().get(sql_tempate)
        self.close()
        return result

    def query(self, **kwargs):
        pass
