from core.handle import BaseHandler
from tornado.websocket import WebSocketHandler
import tornado.gen
import logging


class RoomWebHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('room/index.html', )


class ChatHandler(WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(ChatHandler, self).__init__(*args, **kwargs)
        self.listen()

    @tornado.gen.engine
    def listen(self):
        import tornadoredis
        self.redis_client = tornadoredis.Client()
        self.redis_client.connect()
        yield tornado.gen.Task(self.redis_client.subscribe, 'test_channel')
        self.redis_client.listen(self.on_message)

    def open(self):
        logging.info("on new cline")

    def on_message(self, message):
        print(message)
        if not isinstance(message, unicode):
            if message.kind == 'message':
                self.write_message(str(message.body))
            if message.kind == 'disconnect':
                # Do not try to reconnect, just send a message back
                # to the client and close the client connection
                self.write_message('The connection terminated '
                                   'due to a Redis server error.')
                self.close()
        else:
            self.write_message(message)

    def on_close(self):
        if self.redis_client.subscribed:
            self.redis_client.unsubscribe('test_channel')
            self.redis_client.disconnect()
