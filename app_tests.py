import unittest
import app as tested_app
import json
from test_data.data import User


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_user_api_endpoint(self):
        r = self.app.get(User.URL)
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()