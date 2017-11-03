"Contains all the tests for RecipeNote app"
from recipenote import app
import unittest

class FlaskTestCase(unittest.TestCase):
    "Handles testing in our app"
    
    def test_index_page_loads_properly(self):
        "Tests if the index page loads properly"
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index_page_contains_right_content(self):
        "Tests if the index page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertIn(b'Are you into preparing your food?', response.data)

    def test_register_page_loads(self):
        "tests to see that the register page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_register_page_contains_right_content(self):
        "Tests if the register page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertIn(b'Please Register to continue', response.data)

    def test_login_page_loads(self):
        "tests to see that the login page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_contains_right_content(self):
        "Tests if the login page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertIn(b'Please Login to continue', response.data)

    def test_recipes_page_loads(self):
        "tests to see that the recipes page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/recipes', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipes_page_contains_right_content(self):
        "Tests if the recipes page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/recipes', content_type='html/text')
        self.assertIn(b'Recipes', response.data)

    def test_recipes_add_page_loads(self):
        "tests to see that the recipes_add page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/recipes_add', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipes_add_page_contains_right_content(self):
        "Tests if the recipes_add page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/recipes_add', content_type='html/text')
        self.assertIn(b'Create a new Recipe', response.data)

    def test_recipe_edit_page_loads(self):
        "tests to see that the recipe_edit page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/recipe_edit', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipe_edit_page_contains_right_content(self):
        "Tests if the recipe_edit page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/recipe_edit', content_type='html/text')
        self.assertIn(b'Edit Your Recipe', response.data)

    def test_recipe_detail_page_loads(self):
        "tests to see that the recipe_detail page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/recipe_detail', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_page_contains_right_content(self):
        "Tests if the recipe_detail page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/recipe_detail', content_type='html/text')
        self.assertIn(b'Recipe Details', response.data)

    def test_category_page_loads(self):
        "tests to see that the category page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/category', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_category_page_contains_right_content(self):
        "Tests if the category page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/category', content_type='html/text')
        self.assertIn(b'Your Categories', response.data)

    def test_category_edit_page_loads(self):
        "tests to see that the category_edit page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/category_edit', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_category_edit_page_contains_right_content(self):
        "Tests if the category_edit page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/category_edit', content_type='html/text')
        self.assertIn(b'Edit Category', response.data)

    def test_category_create_page_loads(self):
        "tests to see that the category_create page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/category_create', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_category_create_page_contains_right_content(self):
        "Tests if the category_create page contains the right content"
        tester = app.test_client(self)
        response = tester.get('/category_create', content_type='html/text')
        self.assertIn(b'Create a new Category', response.data)
    
  
if __name__ == "__main__":
    unittest.main()
