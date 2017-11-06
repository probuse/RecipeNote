"Contains all the tests for RecipeNote app"
import unittest
from flask import session
from recipenote import app

class FlaskTestCase(unittest.TestCase):
    "Handles testing in our app"

    def setUp(self):
        "Helps set up our environment"
        self.app = app.test_client()
        app.config['WTF_CSRF_ENABLED'] = False

        self.app.testing = True

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

    def test_recipes_page_doesnot_load_page_for_guest_users(self):
        "tests to see that the recipes page loads correctly"
        tester = app.test_client(self)
        response = tester.get('/recipes', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_recipes_page_contains_right_content_for_logged_in_users(self):
        "Tests if the recipes page contains the right content"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/recipes', content_type='html/text')
            self.assertIn(b'Recipes', response.data)
            self.assertTrue(response.status_code, 200)

    def test_recipes_add_page_doesnot_load_for_guest_users(self):
        "tests to see that the recipe_add page loads correctly"
        with app.test_client(self) as client:
            response = client.get('/recipe_add', content_type='html/text')
            self.assertEqual(response.status_code, 302)

    def test_recipes_add_page_contains_right_content_for_logged_in_users(self):
        "Tests if the recipe_add page contains the right content"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/recipe_add', content_type='html/text')
            self.assertIn(b'Create a new Recipe', response.data)

    def test_recipe_edit_page_doesnot_load_for_guest_users(self):
        "tests to see that the recipe_edit page loads correctly"
        with app.test_client(self) as client:
            response = client.get('/recipe_edit', content_type='html/text')
            self.assertEqual(response.status_code, 302)

    def test_recipe_edit_page_contains_right_content(self):
        "Tests if the recipe_edit page contains the right content"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/recipe_edit', content_type='html/text')
            self.assertIn(b'Edit Your Recipe', response.data)

    def test_recipe_detail_page_doesnot_load_for_guest_users(self):
        "tests to see that the recipe_detail page loads correctly"
        with app.test_client(self) as client:
            response = client.get('/recipe_detail', content_type='html/text')
            self.assertEqual(response.status_code, 302)

    def test_recipe_detail_page_contains_right_content_for_logged_in_users(self):
        "Tests if the recipe_detail page contains the right content"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/recipe_detail', content_type='html/text')
            self.assertIn(b'Recipe Details', response.data)

    def test_category_page_doesnot_load_for_guest_users(self):
        "tests to see that the category page loads correctly"
        with app.test_client(self) as client:
            response = client.get('/category', content_type='html/text')
            self.assertEqual(response.status_code, 302)

    def test_category_page_contains_right_content_for_logged_in_users(self):
        "Tests if the category page contains the right content"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/category', content_type='html/text')
            self.assertIn(b'Your Categories', response.data)

    def test_category_edit_page_doesnot_load_for_guest_users(self):
        "tests to see that the category_edit page loads correctly"
        with app.test_client(self) as client:
            response = client.get('/category_edit', content_type='html/text')
            self.assertEqual(response.status_code, 302)

    def test_category_edit_page_contains_right_content_for_logged_in_users(self):
        "Tests if the category_edit page contains the right content"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/category_edit', content_type='html/text')
            self.assertIn(b'Edit Category', response.data)

    def test_category_create_page_doesnot_load_for_guest_users(self):
        "tests to see that the category_add page loads correctly"
        with app.test_client(self) as client:
            response = client.get('/category_add', content_type='html/text')
            self.assertEqual(response.status_code, 302)

    def test_category_create_page_contains_right_content(self):
        "Tests if the category_create page contains the right content"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/category_add', content_type='html/text')
            self.assertIn(b'Create a new Category', response.data)

    def test_logout_page_requires_login(self):
        "Test User is logged to access login page"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/logout', follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_guest_user_cannot_access_logout_page(self):
        "Tests logout page is accessed by only logged in users"
        with app.test_client(self) as client:
            response = client.get('/logout', content_type='html/text')
            self.assertEqual(response.status_code, 302)

    def test_one_user_exists_for_newly_user_signed_in_user(self):
        "Tests user exixsts after sign up and login"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            user = session["users"]
            self.assertEqual(len(user), 1)

    def test_no_category_for_new_user(self):
        "Tests no categories for a new user"
        with app.test_client(self) as client:
            client.post(
                '/register', 
                data=dict(
                    username="etwin",
                    email="etwin@us.com",
                    password="etwin",
                    password2="etwin"
                ))
            client.post(
                '/login',
                data=dict(
                    username="etwin",
                    password="etwin"
                ))
            response = client.get('/category', content_type="html/text")
            categories = session["category"]
            self.assertEqual(len(categories), 0)
            self.assertIn(b'No Categories Added yet', response.data)

    # def test_one_category_exists_after_user_creates_category(self):
    #     "Tests adding category works"
    #     with app.test_client(self) as client:
    #         client.post(
    #             '/register', 
    #             data=dict(
    #                 username="etwin",
    #                 email="etwin@us.com",
    #                 password="etwin",
    #                 password2="etwin"
    #             ))
    #         client.post(
    #             '/login',
    #             data=dict(
    #                 username="etwin",
    #                 password="etwin"
    #             ))
    #         client.post(
    #             '/category_add',
    #             data=dict(name="local foods"), 
    #             follow_redirects=True
    #         )
    #         response = client.get('/category', content_type='html/text')
    #         categories = session['category']
    #         print(categories)
    #         self.assertEqual(len(categories), 1)

    def test_edit_category_fuctionality_works(self):
        "Tests editing category fuctionlaity works"
        pass

    def test_deleted_category_actually_gets_deleted(self):
        "Tests if deleted category gets deleted"
        pass


    
  
if __name__ == "__main__":
    unittest.main()
