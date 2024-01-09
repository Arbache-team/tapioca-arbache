import responses
import status
import pytest

from tapioca_arbache.tapioca_arbache import OauthClient


@pytest.fixture
def autenticador():
    return {
        "access_token": "ZRyFBfh7G1OJ8dPvDjsoCGc9jxYqBM",
        "expires_in": 36000,
        "token_type": "Bearer",
        "scope": "read write groups",
        "refresh_token": "xb8oifIiYLYmFhtSflxAxAKXSOj4Mo"
    }


@responses.activate
def test_autenticar(base_url, autenticador):
    responses.add(
        method=responses.POST,
        url=f"{base_url}/backend/oauth-token/",
        status=status.HTTP_200_OK,
        json=autenticador
    )

    data = {
        'client_id': 'WvBxFof28HxjQjk0ryl94bAmpylKqie7kReNWHny',
        'grant_type': 'password',
        'username': 'testandinho@arbache.com',
        'password': 'teste123'
    }

    oauth_client = OauthClient(url='https://teste.com.br')

    response = oauth_client.oauth_token().post(data=data)

    assert response().status_code == status.HTTP_200_OK
    assert response().data == autenticador


@responses.activate
def test_autenticar_sem_client_id(base_url):
    data = {
        'grant_type': 'password',
        'username': 'testandinho@arbache.com',
        'password': 'teste123'
    }
    oauth_client = OauthClient(url='https://teste.com.br')
    try:
        oauth_client.oauth_token().post(data=data)
    except Exception as erro:
        assert isinstance(erro, AssertionError)


@responses.activate
def test_autenticar_sem_grant_type(base_url):
    data = {
        'client_id': 'WvBxFof28HxjQjk0ryl94bAmpylKqie7kReNWHny',
        'username': 'testandinho@arbache.com',
        'password': 'teste123'
    }
    oauth_client = OauthClient(url='https://teste.com.br')
    try:
        oauth_client.oauth_token().post(data=data)
    except Exception as erro:
        assert isinstance(erro, AssertionError)


@responses.activate
def test_autenticar_sem_username(base_url):
    data = {
        'client_id': 'WvBxFof28HxjQjk0ryl94bAmpylKqie7kReNWHny',
        'grant_type': 'password',
        'password': 'teste123'
    }
    oauth_client = OauthClient(url='https://teste.com.br')
    try:
        oauth_client.oauth_token().post(data=data)
    except Exception as erro:
        assert isinstance(erro, AssertionError)


@responses.activate
def test_autenticar_sem_password(base_url):
    data = {
        'client_id': 'WvBxFof28HxjQjk0ryl94bAmpylKqie7kReNWHny',
        'grabt_type': 'password',
        'username': 'testandinho@arbache.com'
    }
    oauth_client = OauthClient(url='https://teste.com.br')
    try:
        oauth_client.oauth_token().post(data=data)
    except Exception as erro:
        assert isinstance(erro, AssertionError)


@responses.activate
def test_autenticar_sem_body(base_url):
    oauth_client = OauthClient(url='https://teste.com.br')
    try:
        oauth_client.oauth_token().post()
    except Exception as erro:
        assert isinstance(erro, AssertionError)
