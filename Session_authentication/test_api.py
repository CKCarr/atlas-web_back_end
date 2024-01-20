import unittest
import requests_mock
import base64
import requests
from api.v1.app import app

class TestApi(unittest.TestCase):
    def setUp(self):
        self.user_email = "u3@hbtn.io"
        self.user_clear_pwd = "pwd"
        self.basic_clear = "{}:{}".format(self.user_email, self.user_clear_pwd)
        self.auth_header = {
            'Authorization': "Basic {}".format(
                base64.b64encode(self.basic_clear.encode('utf-8')).decode("utf-8")
            )
        }

    @requests_mock.Mocker()
    def test_get_user_me(self, m):
        url = 'http://0.0.0.0:3456/api/v1/users/me'
        m.get(url, json={'email': self.user_email}, status_code=200, headers={'content-type': 'application/json'})

        with app.test_client() as client:
            response = client.get('/api/v1/users/me', headers=self.auth_header)
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "application/json")
            response_json = response.get_json()
            
            self.assertIsInstance(response_json, dict)
            self.assertEqual(response_json.get('email'), self.user_email)
            
if __name__ == '__main__':
    unittest.main()
