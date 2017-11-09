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
        self.user_recipes = {}

    def create_category(self, category_name):
        "creates a category"
        category = Category(category_name)
        self.user_categories[category.name] = []
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
            raise KeyError("{} does not exist".format(category_name))
        recipe = Recipe(recipe_name, recipe_prep_method)
        self.user_categories[category_name].append(recipe_name)
        self.user_recipes[recipe_name] = recipe_prep_method.splitlines()
        return recipe

    def edit_recipe_name(self, old_name, new_name):
        "Helps to update a recipe name to a new name"
        print(self.user_recipes)
        if old_name in self.user_recipes.keys():
            self.user_recipes[new_name] = self.user_recipes.pop(old_name)
            for recipe in self.user_categories.values():
                if old_name in recipe:
                    recipe.remove(old_name)
                    recipe.append(new_name)

        else:
            raise KeyError('{} does not exist as a recipe name'.format(old_name))

    def edit_recipe_prep_method(self,recipe, new_method):
        "Updates recipe_prep_method to a new method"
        if recipe in self.user_recipes:
            self.user_recipes[recipe] = new_method

    def delete_recipe(self, recipe_name):
        "Deletes recipe with recipe name"
        for recipes in self.user_categories.keys():
                if recipe_name in self.user_categories[recipes]:
                    del recipe_name
        # del self.user_recipes[recipe_name]
    


