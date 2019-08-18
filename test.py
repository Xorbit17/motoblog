from tornado import template


def get_strings():
    return ["Kaka " + str(i) for i in range(1000)]


loader = template.Loader("templates/")
f = open("result.html", "w")
f.write(loader.load("main.html").generate(
    title="Protput",
    string_list=get_strings(),
    show=True).decode("utf-8"))
f.close()
