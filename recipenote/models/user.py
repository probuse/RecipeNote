"Controls the User Object"

from recipenote.models.category import Category
from recipenote.models.recipe import Recipe

class User(object):
    "controls user object"

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password1 = password
        self.user_categories = {}

    def create_category(self, category_name):
        "creates a category"
        category = Category(category_name)
        self.user_categories[category.name] = {}
        return category

    def edit_category_name(self, old_name, new_name):
        "Helps to edit a category name"
        if old_name in self.user_categories.keys():
            self.user_categories[new_name] = self.user_categories.pop(old_name)

    def delete_category(self, category_name):
        "deletes a category with a name category_name"
        del self.user_categories[category_name]

    def create_recipes(
        self, 
        recipe_name, 
        category_name, 
        recipe_prep_method):
        "Creates a recipe"
        if category_name not in self.user_categories.keys():
            return "{} does not exist".format(category_name)
        recipe = Recipe(recipe_name,category_name, recipe_prep_method.splitlines())
        self.user_categories[category_name][recipe_name] = recipe_prep_method.splitlines()
        return recipe

    def edit_recipe(self, old_name, new_name, new_method):
        "Helps to update a recipe name to a new name"
        for category in self.user_categories:
            if old_name in self.user_categories[category]:
                self.user_categories[category][new_name] = self.user_categories[category].pop(old_name)
                self.user_categories[category][new_name] = new_method.splitlines()
            else:
                return '{} does not exist as a recipe name'.format(old_name)

    def delete_recipe(self, recipe_name):
        "Deletes recipe with recipe name"
        for recipes in self.user_categories.keys():
                if recipe_name in self.user_categories[recipes]:
                    del recipe_name
        # del self.user_recipes[recipe_name]
    


