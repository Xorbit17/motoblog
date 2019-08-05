# Readme
This repository has been created for educational purposed. It serves to learn some basic techniques such as:

* Markdown
* Git
* Github
* Python
* Template engine
* How HTTP works in general
* HTML, Javascript, CSS
* Bootstrap

Please enjoy this simple project.

## Blog concept

The idea of the education project is to make a blog about motorcycles.
The big idea of a blog is displaying articles. The main page should show an interesting overview of different kinds of articles. Any article needs to be displayed in a specific page to make reading it as nice as possible.

These are the different article categories:
* Motorcycle reviews (MOTO)
* Motorcycle gear reviews (GEAR)
* Muzing and ranting (RANT)
* Motorcycle travel (TRAVEL)

An article has these properties aside from its content
* Title
* Categories (See above), can be empty list and more than one
* Publish date
* Last edited date
* Featured (True/False)

These are the pages the blog site will have
* Home page: Overview of different articles, featured articles
* Article list page: Show list of articles from one category
* Article detail page: Show specific article

## Technical design

The general idea is to make it a simple system. Just the file system will be used. The requests will be processed by python scripts using a template engine. The python scripts will scan the file system for all the articles. This would be too slow and not scalable for production grade projects. But for education purposes it is fine. In a later lesson the file system can be replaced by a database of some sort.

## Website design

We downloaded and changed a free template from [Templated](https://templated.co/industrious). Specifically the "Industrious" theme. Big thanks to those guys.
