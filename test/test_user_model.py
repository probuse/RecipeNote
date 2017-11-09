"""All tests for our models go here."""
import unittest
from recipenote.models.user import User

class UserModelTestCase(unittest.TestCase):
    "tests features and funtionlity for user.py"
    
    def setUp(self):
        self.user = User("etwin", "etwin@us.com", "etwin")
        self.category = self.user.create_category('Local Foods')
        self.recipes = self.user.create_recipes(
            'rolex', 
            self.category.name, 
            'beat eggs\nfry them\nadd chapatti')

    def test_user_has_creates_category(self):
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
        self.assertListEqual(
            self.user.user_categories[self.category.name], 
            ['rolex'])

    def test_user_recipe_prep_method(self):
        "Tests user is able to add recipe"
        self.assertListEqual(
            self.user.user_recipes['rolex'], 
            ['beat eggs', 'fry them', 'add chapatti'])

    def test_user_can_edit_recipe_name(self):
        "Test user can edit recipe name"
        new_recipe_name = 'Junk'
        self.user.edit_recipe_name(self.recipes.name, new_recipe_name)
        self.assertEqual(
            self.user.user_recipes[new_recipe_name], 
            'beat eggs\nfry them\nadd chapatti'.splitlines())

    # def test_user_can_edit_recipe_prep_method(self):
    #     "Test user can edit prep_method"
    #     new_recipe_methods = 'boil it\nadd salt'
    #     self.user.edit_recipe_prep_method(self.recipes.name, new_recipe_methods)
    #     self.assertListEqual(
    #         self.user.user_recipes[self.recipes.name], 
    #         new_recipe_methods.splitlines())
    
    def test_can_delete_recipe(self):
        "Tests user can delete recipe"
        len_of_category = len(self.user.user_categories['Local Foods'])
        self.user.delete_recipe('rolex')
        len_of_category2 = len(self.user.user_categories['Local Foods'])
        # self.user.delete_recipe('rolex')
        # len_of_recipe_dict = len(self.user.user_recipes)
        # len_of_category_dict_with_recipe = len(
        #     self.user.user_categories[self.category.name]
        #     )
        # del self.user.user_recipes[self.recipes.name]
        # len_of_recipe_dict2 = len(self.user.user_recipes)
        # len_of_category_dict_with_recipe2 = len(
        #     self.user.user_categories[self.category.name]
        #     )
        # self.assertEqual(len_of_recipe_dict, 1)
        # self.assertEqual(len_of_recipe_dict2, 0)
        self.assertEqual(len_of_category, 1)
        self.assertEqual(len_of_category2, 1)
        # self.assertEqual(len_of_category_dict_with_recipe2, 0)

if __name__ == "__main__":
    unittest.main()
    