"""Tests for the registration page and the process of registration go here"""
import unittest
from recipenote import app

class FlaskTestCase(unittest.TestCase):
    "Handles testing in our registeration"

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


if __name__ == "__main__":
    unittest.main()