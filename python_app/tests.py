"""
Unit tests for the main.py
"""
import unittest

from main import APP


class BasicTests(unittest.TestCase):
    """
    Test cases
    """

    def setUp(self):
        """
            Pre testing setup
        """
        APP.config['TESTING'] = True
        APP.config['DEBUG'] = False
        self.app = APP.test_client()

    def test_index_page(self):
        """
            Tests that index page returns valid response
        """
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_healthcheck(self):
        """
            Tests that healthcheck page returns valid response
        """
        response = self.app.get('/healthcheck', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        """
            Post testing cleanup
        """
        pass

if __name__ == '__main__':
    unittest.main()
