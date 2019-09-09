# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import handlers.page_handlers
import os


# We krijgen een request binnen: "GET index.html"
def make_app():
    return tornado.web.Application([  # LIST OF TUPLES  (regular expression, handler opbject)
        (r"/category-list/", handlers.page_handlers.CategoryListPageHandler),
        (r"/show-article", handlers.page_handlers.ArticlePageHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler,
         {"path": os.path.join(os.path.dirname(__file__), "templates\\static")}
         ),
        (r"/(.*)", handlers.page_handlers.HomePageHandler)
    ])


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
