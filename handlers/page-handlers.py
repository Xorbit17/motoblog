from tornado.web import RequestHandler


"""        (r"/", HomePageHandler),
        (r"/", CategoryListPageHandler),
        (r"/", ArticlePageHandler),"""
class HomePageHandler(RequestHandler):
    def get(self):
        self.write("Placeholder")

class CategoryListPageHandler(RequestHandler):
    def get(self):
        self.write("Placeholder")

class ArticlePageHandler(RequestHandler):
    def get(self):
        self.write("Placeholder")


