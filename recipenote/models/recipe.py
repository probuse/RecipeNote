"Controls the Recipe Object"


class Recipe(object):
    "Controls Recipe object"

    def __init__(self, name, category, prep_method):
        self.name = name
        self.category = category
        self.prep_method = prep_method    