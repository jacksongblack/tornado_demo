from core.handle import BaseHandler


class RoomWebHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('room/index.html',)
