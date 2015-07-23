# encoding:utf-8
import config
import tornadoredis



class Redis(tornadoredis.Client):
    def __init__(self):
        super(Redis, self).__init__(host=config.REDIS_SETTINGS.get('host'), port=int(config.REDIS_SETTINGS.get('port')),
                                    unix_socket_path=config.REDIS_SETTINGS.get('unix_socket_path'),
                                    selected_db=config.REDIS_SETTINGS.get("selected_db"))
