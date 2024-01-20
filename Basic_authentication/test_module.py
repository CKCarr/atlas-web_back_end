
#!/usr/bin/python3
""" Check response
"""
# test_basic_auth.py

from api.v1.auth.basic_auth import BasicAuth

def test_user_object_from_credentials():
    """Test user_object_from_credentials with non-existent user email."""
    ba = BasicAuth()
    res = ba.user_object_from_credentials("u1@gmail.com", "pwd")
    assert res is None, "user_object_from_credentials must return None if 'user_email' is not linked to any user"
