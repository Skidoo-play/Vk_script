import unittest
import app as tested_app
import json


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_user_api_endpoint(self):
        r = self.app.get("/api/user?user_ids=shzfrnia")
        self.assertEqual(r.json, {
            "avatar": "https://sun9-68.userapi.com/c856032/v856032090/108f51/ObW5ybDwiZ8.jpg?ava=1",
            "days_offline": None,
            "first_name": "Mikhail",
            "id": 135480774,
            "is_deactivated": None,
            "is_online": False,
            "last_name": "Ulyakov",
            "last_seen": None,
            "link": "https://vk.com/id135480774"
        })

if __name__ == '__main__':
    unittest.main()