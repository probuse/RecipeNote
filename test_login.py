"""Tests for the login page and the process of login go here"""
import unittest

from recipenote import app

class FlaskTestCase(unittest.TestCase):
    "Handles testing in our registeration"

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
        

if __name__ == "__main__":
    unittest.main()
    