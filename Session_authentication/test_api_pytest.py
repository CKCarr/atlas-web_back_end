# test_api_pytest.py
import requests_mock
import base64
import requests
from api.v1.app import app

user_email = "u3@hbtn.io"
user_clear_pwd = "pwd"
basic_clear = "{}:{}".format(user_email, user_clear_pwd)
auth_header = {
    'Authorization': "Basic {}".format(
        base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")
    )
}

def test_get_user_me():
    url = 'http://0.0.0.0:3456/api/v1/users/me'
    
    with requests_mock.Mocker() as m:
        m.get(url, json={'email': user_email}, status_code=200, headers={'content-type': 'application/json'})
        
        with app.test_client() as client:
            response = client.get('/api/v1/users/me', headers=auth_header)
            
            assert response.status_code == 200
            assert response.content_type == "application/json"
            response_json = response.get_json()
            
            assert isinstance(response_json, dict)
            assert response_json.get('email') == user_email
