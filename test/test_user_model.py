"""All tests for our models go here."""
import unittest
from recipenote.models.user import User

class UserModelTestCase(unittest.TestCase):
    "tests features and funtionlity for user.py"
    
    def setUp(self):
        self.user = User("etwin", "etwin@us.com", "etwin")
        self.category = self.user.create_category('Local Foods')

    def test_user_has_creates_category(self):
        "Tests to see user has created a category"
        self.assertEqual(self.category.name, "Local Foods")

    def test_user_can_edit_category_name(self):
        "Tests user can edit category name"
        category = self.user.create_category('Local Foods')
        new_name = 'Locals'
        self.user.edit_category_name(category.name, new_name)
        self.assertIn(new_name, self.user.user_categories)

    def test_user_can_delete_category(self):
        "Tests user can delete category"
        category = self.user.create_category('Local Foods')
        num_categories1 = len(self.user.user_categories)
        self.user.delete_category(category.name)
        num_categories2 = len(self.user.user_categories)
        self.assertEqual(num_categories1, 1)
        self.assertEqual(num_categories2, 0)

    def test_user_can_add_recipe(self):
        "Tests user is able to add recipe"
        category = self.user.create_category('Local Foods')
        recipes = self.user.create_recipes(
            'rolex', 
            category.name, 
            'beat eggs\nfry them\add chapatti')
        self.assertListEqual(
            self.user.user_categories[category.name], 
            ['rolex'])

    def test_user_recipe_prep_method(self):
        "Tests user is able to add recipe"
        category = self.user.create_category('Local Foods')
        recipes = self.user.create_recipes(
            'rolex', 
            category.name, 
            'beat eggs\nfry them\nadd chapatti')
        self.assertListEqual(
            self.user.user_recipes['rolex'], 
            ['beat eggs', 'fry them', 'add chapatti'])


    def test_user_can_edit_recipe_name(self):
        "Test user can edit recipe name"
        category = self.user.create_category('Local Foods')
        recipes = self.user.create_recipes(
            'rolex', 
            category.name, 
            'beat eggs\nfry them\nadd chapatti')
        new_recipe_name = 'Junk'
        self.user.edit_category_name(recipes.name, new_recipe_name)
        self.assertEqual(category.name, 'Junk')

    def test_user_can_edit_recipe_prep_method(self):
        "Test user can edit prep_method"
        pass
    
    def test_can_delete_recipe(self):
        "Tests user can delete recipe"
        pass

if __name__ == "__main__":
    unittest.main()
    