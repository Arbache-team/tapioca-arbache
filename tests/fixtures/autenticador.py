import pytest


@pytest.fixture
def autenticador():
    return {
        "access_token": "ZRyFBfh7G1OJ8dPvDjsoCGc9jxYqBM",
        "expires_in": 36000,
        "token_type": "Bearer",
        "scope": "read write groups",
        "refresh_token": "xb8oifIiYLYmFhtSflxAxAKXSOj4Mo"
    }