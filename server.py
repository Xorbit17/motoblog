# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import handlers.page_handlers
import os

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")


# We krijgen een request binnen: "GET index.html"
def make_app():
    app = tornado.web.Application([  # LIST OF TUPLES  (regular expression, handler opbject)
        (r"/home", handlers.page_handlers.HomePageHandler),
        (r"/categories", handlers.page_handlers.CategoryListPageHandler),
        (r"/show-article/(.*)", handlers.page_handlers.ArticlePageHandler),  # Hander that renders an article
        (r"/articles/(.*)", tornado.web.StaticFileHandler,  # Static file hander for images in articles
         {"path": os.path.join(os.path.dirname(__file__), "articles")}
         ),
        (r"/static/(.*)", tornado.web.StaticFileHandler,  # Static file hander for site assets such as css, js, images
         {"path": os.path.join(os.path.dirname(__file__), "templates\\static")}
         ),
        (r"/", handlers.page_handlers.HomePageHandler)
    ])
    app.settings["template_path"] = TEMPLATE_PATH
    return app


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()  # Oneindig wachten

# In den beginne
# Enkel HTML
# Universiteiten soort encyclopedie
# HTTP: Protocol - HTTP geeft een commando met headers mee
#   GET: Documentje opvragen
#   POST: Documentje er in steken!! Response body
#   DELETE, PUT, ... Niet veel meer gebruikt

# Antwoord: Status code: 200 OK. 401 Page not found
# Antwoord REDIRECT
# Respons: Bevat de info dat je wilt zien: HTML, CSS, JS, IMG, JSON, XML, Binair
# Resonses bevatten ook headers
