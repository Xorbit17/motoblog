# -*- coding: utf-8 -*-
from tornado.web import RequestHandler
import os
import markdown2, json
import datetime

from categories import Category

# Load articles data. Because of this the server needs to be restarted every time
# the articles are changed. But this is only a simple website.

# Load the JSON in to memory. This is our database, kind of
articles_data = json.load(
    open(os.path.join(os.path.dirname(__file__), "..\\articles\\articles.json"), "rb")
)  # type: dict

# Make a datastructure for our navigation
default_nav = {
    "navitems": [
        dict(link="/home", caption="Home"),
        dict(link="/categories", caption="Articles by category"),
    ],
    "dropdowns": [

    ]
}
for c in Category:
    cat_list = []
    for a in articles_data.keys():
        if c.name in articles_data[a]["category"]:
            cat_list.append(a)

    if len(cat_list) > 0:
        default_nav["dropdowns"].append({"caption_dropdown": c.value, "items": []})
        for a in cat_list:
            default_nav["dropdowns"][-1]["items"].append(dict(link="articles/" + a, caption=articles_data[a]["title"]))

# Make a data structure to look up articles by creation date
# A dict mapping a python date object to an article link
date_created_articles = {}
for a in articles_data.keys():
    date_created = datetime.datetime.fromisoformat(articles_data[a]["date-created"])
    date_created_articles[date_created] = a

# Make a sorted list of all dates
sorted_list_of_dates = sorted(date_created_articles.keys())

# Make a data structure associating a categry with a list of article links
category_articles = {}
for c in Category:
    cat_list = []
    for a in articles_data.keys():
        if c.name in articles_data[a]["category"]:
            cat_list.append(a)

    category_articles[c] = cat_list


# Make


def get_template_path(template_name):
    return os.path.join(os.path.dirname(__file__), "..\\templates\\" + template_name)


class HomePageHandler(RequestHandler):

    def get(self):
        # Make a list of recent articles with no more then 5 articles
        # Technically this code could be exeucted outside of this function
        # But I put it here for clarity
        recent_articles_sorted = []
        for num, date in enumerate(sorted_list_of_dates):
            if num >= 5:
                break
            link = date_created_articles[date]
            recent_articles_sorted.append(articles_data[link])

        self.render(get_template_path("home.html"),
                    page_title="MotoBLOG - Homepage",
                    nav=default_nav,
                    recent_articles=recent_articles_sorted
                    )


class CategoryListPageHandler(RequestHandler):
    def get(self):
        category_article_data = []
        for c in Category:
            category_article_list = []
            for article_link in category_articles[c]:
                category_article_list.append(articles_data[article_link])

            category_article_data.append({
                "category-title": c.value,
                "articles_list": category_article_list
            })

        self.render(get_template_path("categories.html"),
                    page_title="MotoBLOG - Homepage",
                    nav=default_nav,
                    category_article_data=category_article_data
                    )


class ArticlePageHandler(RequestHandler):
    md = markdown2.Markdown()

    def get(self, article_link):
        # Select article
        if article_link in articles_data.keys():
            article_data = articles_data[article_link]
            article_path = "..\\articles\\{0}\\article.md".format(article_data["file-folder"])

            # Open markdown file, read it, convert it to html, close the file
            f = open(os.path.join(os.path.dirname(__file__), article_path), "rb")
            body_html = self.md.convert(f.read())
            f.close()

            # Render the template. Please mind the 'raw' function in the template for body_html
            self.render(get_template_path("article.html"),
                        page_title="MotoBLOG - " + article_data["title"],
                        nav=default_nav,
                        article_data=article_data,
                        body_html=body_html
                        )
        else:
            # Article link not found in list defined by articles.json... Show error page
            error_body = "The article with link '' was not found. Please check the url. If a link is broken please report it.".format(
                article_link)
            self.render(get_template_path("error.html"),
                        page_title="Error page",
                        error_title="Article not found",
                        error_body=error_body)
