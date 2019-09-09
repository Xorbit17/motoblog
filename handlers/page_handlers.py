# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
import os
import markdown2, json

from categories import Category

# Load articles data. Because of this the server needs to be restarted every time
# the articles are changed. But this is only a simple website.
articles_data = json.load(
    open(os.path.join(os.path.dirname(__file__), "..\\articles\\articles.json"), "rb")
)  # type: dict

default_nav = {
    "nav_items": [
        dict(link="home", caption="Home"),
        dict(link="categories", caption="Articles by category"),
    ],
    "dropdowns": [

    ]
}
for c in Category:
    cat_list = []
    for a in articles_data.keys():
        if c.__name__ in articles_data[a]["category"]:
            cat_list.append(a)

    if len(cat_list) > 0:
        default_nav["dropdowns"].append({"caption_dropdown": c.value(), "items": []})
        for a in cat_list:
            default_nav["dropdowns"][-1]["items"].append(dict(link="articles/" + a, caption=articles_data[a]["title"]))


class HomePageHandler(RequestHandler):
    def get(self, match):
        f = open(os.path.join(os.path.dirname(__file__), "..\\templates\\ex.html"), "rb")
        self.write(f.read())
        f.close()


class CategoryListPageHandler(RequestHandler):
    def get(self):
        self.write("Placeholder")


class ArticlePageHandler(RequestHandler):
    md = markdown2.Markdown()

    def get(self, article_name):
        # load article
        if article_name in articles_data.keys():
            article_data = articles_data[article_name]

        f = open(os.path.join(os.path.dirname(__file__), "..\\articles\\{0}\\{0}.md"), "rb")
        body_html = self.md.convert(f.readlines())

