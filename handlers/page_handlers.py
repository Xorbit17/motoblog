# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
import os


class HomePageHandler(RequestHandler):
    def get(self, match):
        f = open(os.path.join(os.path.dirname(__file__), "..\\static\\ex.html"), "rb")
        self.write(f.read())
        f.close()



class CategoryListPageHandler(RequestHandler):
    def get(self):
        self.write("Placeholder")


class ArticlePageHandler(RequestHandler):
    def get(self):
        self.write("Placeholder")
