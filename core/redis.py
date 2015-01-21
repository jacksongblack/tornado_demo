# encoding:utf-8
import redis
import config


class RedisBase(object):
    @staticmethod
    def connection(host=config.REDIS_SETTINGS.get("host"), port=config.REDIS_SETTINGS.get("port")):
        return redis.Redis(host, port)

    @classmethod
    def get(cls, key):
        r = cls.connection()
        value = r.get(key)
        return cls(key, value)

    @classmethod
    def create(cls, key, value):
        r = cls.connection()
        value = r.set(key, value)
        return cls(key, value)

    def __init__(self, key, value):
        self.__redis = self.connection().pipeline()
        self.__key = key
        setattr(self, key, value)

    def update(self, value):
        return self.__redis.set(self.__key, value)

    def execute(self):
        self.__redis.execute()
