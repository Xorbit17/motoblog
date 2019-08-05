# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import handlers.page_handlers
import os


def make_app():
    return tornado.web.Application([
        (r"/", handlers.page_handlers.HomePageHandler),
        (r"/category-list/", handlers.page_handlers.CategoryListPageHandler),
        (r"/show-article", handlers.page_handlers.ArticlePageHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler,
         {"path": os.path.join(os.path.dirname(__file__), "static")}
        )

    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
