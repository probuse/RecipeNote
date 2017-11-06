"Controls the User Object"
# email will act as a unique key


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
        self.user_categories[category_name] = []
        return self.user_categories

    def edit_category(self, old_name, new_name):
        "Helps to edit a category name"
        pass

    def delete_category(self, category_name):
        "deletes a category with a name category_name"
        pass

    def create_recipes(
        self, 
        recipe_name, 
        category_name, 
        recipe_prep_method):
        "Creates a recipe"
        pass

    def edit_recipe_name(self, old_name, new_name):
        "Helps to update a recipe name to a new name"
        pass

    def edit_recipe_prep_method(self, old_method, new_method):
        "Updates recipe_prep_method to a new method"
        pass

    def delete_recipe(self, recipe_name):
        "Deletes recipe with recipe name"
        pass
    


