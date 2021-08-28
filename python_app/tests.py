import unittest

from main import app, index, health_check


class BasicTests(unittest.TestCase):

	def setUp(self):
		"""
			Pre testing setup
		"""
		app.config['TESTING'] = True
		app.config['DEBUG'] = False
		self.app = app.test_client()

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