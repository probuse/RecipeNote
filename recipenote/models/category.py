"""Controls the Category Object"""


class Category(object):
    "Controls Recipe object"

    def __init__(self, name):
        self.name = name
        self.recipes = []