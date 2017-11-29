"""All tests for our models go here."""
import unittest
from recipenote.models.user import User

class UserModelTestCase(unittest.TestCase):
    "tests features and funtionlity for user.py"
    
    def setUp(self):
        self.user = User("etwin", "etwin@us.com", "etwin")
        self.category = self.user.create_category('Local Foods')
        self.recipe = self.user.create_recipes(
            "rolex", self.category.name, 'beat eggs\nfry them\nadd chapatti')
        # self.recipes = self.user.create_recipes(
        #     'rolex', 
        #     self.category.name, 
        #     'beat eggs\nfry them\nadd chapatti')

    def test_user_has_created_category(self):
        "Tests to see user has created a category"
        self.assertEqual(self.category.name, "Local Foods")

    def test_user_can_edit_category_name(self):
        "Tests user can edit category name"
        new_name = 'Locals'
        self.user.edit_category_name(self.category.name, new_name)
        self.assertIn(new_name, self.user.user_categories)

    def test_user_can_delete_category(self):
        "Tests user can delete category"
        num_categories1 = len(self.user.user_categories)
        self.user.delete_category(self.category.name)
        num_categories2 = len(self.user.user_categories)
        self.assertEqual(num_categories1, 1)
        self.assertEqual(num_categories2, 0)

    def test_user_can_add_recipe(self):
        "Tests user is able to add recipe"
        num_of_recipes = len(self.user.user_categories[self.category.name])
        self.user.create_recipes("ugali", self.category.name, "boil beans\nboil maize\nadd salt")
        num_of_recipes2 = len(self.user.user_categories[self.category.name])
        self.assertEqual( num_of_recipes, 1)
        self.assertEqual( num_of_recipes2, 2)

    def test_user_can_edit_recipe(self):
        "Test user can edit recipe"
        new_recipe_name = 'Junk'
        self.user.edit_recipe(
            self.recipe.name, new_recipe_name, 'beat eggs\nfry them\nadd chapatti')
        self.assertEqual(
            self.user.user_categories['Local Foods'][new_recipe_name], 
            'beat eggs\nfry them\nadd chapatti'.splitlines())
    
    def test_can_delete_recipe(self):
        "Tests user can delete recipe"
        len_of_category = len(self.user.user_categories['Local Foods'])
        self.user.delete_recipe('rolex')
        len_of_category2 = len(self.user.user_categories['Local Foods'])
        self.assertEqual(len_of_category, 1)
        self.assertEqual(len_of_category2, 0)

if __name__ == "__main__":
    unittest.main()
    