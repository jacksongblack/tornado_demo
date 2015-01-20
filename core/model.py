# encoding:utf-8
from torndb import Connection
import config


class BaseModel(object):
    _TABLE_NAME = None
    _KEYS = None

    def __init__(self, **fields):
        for key in self._KEYS:
            setattr(self, key, fields.get(key))

    @classmethod
    def connection(cls):
        cls._db = Connection(config.MYSQL_SETTINGS.get('host'), config.MYSQL_SETTINGS.get("database_name"),
                             user=config.MYSQL_SETTINGS.get("username"), password=config.MYSQL_SETTINGS.get("password"))
        return cls._db

    @classmethod
    def close(cls):
        cls._db.close()

    @classmethod
    def get(cls, **kwargs):
        '''
        生成查询列sql语句
        :param kwargs: 字段与值
        :return:类的实例
        '''
        sql_template = 'SELECT * FROM %s ' % (cls._TABLE_NAME,)
        num = 1
        for field_name, field_value in kwargs.items():
            if field_name in cls._KEYS:
                if num is 1:
                    sql_template = '%s %s %s=%s' % (sql_template, 'where', str(field_name), str(field_value),)
                else:
                    sql_template = '%s %s %s=%s' % (sql_template, "and", str(field_name), str(field_value),)
                num += 1
        result = cls.connection().get(sql_template)
        cls.close()
        return cls(**result)

    @classmethod
    def where(cls, field, operation, val):
        op_dict = {
            '=': ""
        }
        sql_tempate = 'SELECT * FROM %s' % (cls._TABLE_NAME,)

