"""All tests for the category model go here."""
import unittest
from recipenote.models.user import Category

class CategoryModelTestCase(unittest.TestCase):
    "tests functionality and features of category.py"

    def setUp(self):
        pass

    def test_no_category_for_new_user(self):
        "Tests no categories for a new user"
        pass

    def test_no_recipes_in_new_category(self):
        "Tests if new category has no recipes"
        pass

    def test_category_contains_recipes_once_added(self):
        "Tests if added recipes exist in this category"
        pass
    
    def test_category_belongs_to_user(self):
        "Tests a category has a user"
        pass

    def test_recipe_is_deleted_when_its__category_is_deleted(self):
        "Tests deleted category does not mean recipes are deleted"
        pass

if __name__ == "__main__":
    unittest.main()