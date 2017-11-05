"""All tests for the recipe model go here"""
import unittest

class RecipeTestCase(unittest.TestCase):
    "Tests features and functionality for recipe.py"

    def setUp(self):
        pass

    def test_category_exists_before_recipe_is_added(self):
        "Tests category exists before a category is added to it"
        pass

    def test_recipe_has_all_required_attributes_to_create_it(self):
        "Tests new recipe has all required_attributes as it is being created."
        pass

    def test_recipe_names_are_unique(self):
        "Tests all recipes have unique names"
        pass

    def test_deleted_recipe_no_longer_exists(self):
        "Tests deleted recipes actually get deleted"
        pass

    def user_has_no_recipes_in_category_before_recipes_are_created(self):
        "Tests that before a user has created any recipes, no recipes exist"
        pass


if __name__ == "__main__":
    unittest.main()
