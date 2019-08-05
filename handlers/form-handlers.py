from tornado.web import RequestHandler


class CommentHandler(RequestHandler):
    def post(self, *args, **kwargs):
        self.write("true")

    def get(self):
        self.write("[]")
