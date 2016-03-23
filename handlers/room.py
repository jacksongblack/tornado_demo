# encoding:utf-8
from core.handle import BaseHandler
from tornado.websocket import WebSocketHandler
from core.redis import Redis
import tornadoredis
import tornado.gen
import logging
import tornado.escape
import sys


class RoomWebHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('room/index.html', )

    def post(self, *args, **kwargs):
        message = self.get_argument('message')
        Redis().publish('test_channel', message)
        self.set_header('Content-Type', 'text/plain')
        self.write('sent: %s' % (message,))


class ChatHandler(WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(ChatHandler, self).__init__(*args, **kwargs)
        self.listen()

    @tornado.gen.engine
    def listen(self):
        self.redis_client = Redis()
        self.redis_client.connect()
        yield tornado.gen.Task(self.redis_client.subscribe, 'test_channel')
        self.redis_client.subscribed = True
        self.redis_client.listen(self.on_messages_published)

    def open(self):
        logging.info("on new cline")

    def on_messages_published(self, message):
        if not isinstance(message, unicode):
            if isinstance(message, tornadoredis.exceptions.RequestError):
                self.write_message(message.message)
            else:
                if message.kind == "subscribe":
                    self.write_message("进入%s号房间" % (str(message.channel)))
                if message.kind == 'message':
                    self.write_message(str(message.body))
                if message.kind == 'disconnect':
                    # Do not try to reconnect, just send a message back
                    # to the client and close the client connection
                    self.write_message('The connection terminated '
                                       'due to a Redis server error.')
                    self.close()

    def on_message(self, message):
        logging.info('Received new message %r', message)
        try:
            # Convert to JSON-literal.
            message_encoded = tornado.escape.json_encode(message)
            # Persistently store message in Redis.
            # Publish message in Redis channel.
            redis = Redis()
            redis.publish('test_channel',message_encoded)
            self.write_message(message_encoded)
        except Exception, err:
            e = str(sys.exc_info()[0])
            # Send an error back to client.
            self.write_message({'error': 1, 'textStatus': 'Error writing to database: ' + str(err)})
            return

        # Send message through the socket to indicate a successful operation.
        self.write_message(message)
        return

    def on_close(self):
        logging.info("socket closed, cleaning up resources now")
        if hasattr(self, 'redis_client'):
            from threading import Timer
            if self.redis_client.subscribed:
                self.redis_client.unsubscribe('test_channel')
                t = Timer(0.1, self.redis_client.disconnect)
                t.start()
