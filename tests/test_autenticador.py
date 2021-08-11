from tapioca_arbache.tapioca_arbache import OauthClient
from tests.fixtures.autenticador import autenticador
import responses
import status


@responses.activate
def test_autenticar(oauth_client, crm_base_url, autenticador):
    responses.add(
        method=responses.POST,
        url=f"{crm_base_url}/backend/oauth-token/",
        status=status.HTTP_200_OK,
        json=autenticador
    )

    response = oauth_client.oauth_token().post()

    assert response().status_code == status.HTTP_200_OK
    assert response().data == autenticador


@responses.activate
def test_autenticar_sem_client_id(crm_base_url, autenticador):
    oauth_client =  OauthClient(
        grant_type='password',
        username='testandinho@arbache.com',
        password='teste123'
    )
    try:
        response = oauth_client.oauth_token().post()
    except Exception as erro:
        assert isinstance(erro, AssertionError)


@responses.activate
def test_autenticar_sem_grant_type(crm_base_url, autenticador):
    oauth_client =  OauthClient(
        client_id='WvBxFof28HxjQjk0ryl94bAmpylKqie7kReNWHny',
        username='testandinho@arbache.com',
        password='teste123'
    )
    try:
        response = oauth_client.oauth_token().post()
    except Exception as erro:
        assert isinstance(erro, AssertionError)


@responses.activate
def test_autenticar_sem_username(crm_base_url, autenticador):
    oauth_client =  OauthClient(
        client_id='WvBxFof28HxjQjk0ryl94bAmpylKqie7kReNWHny',
        grant_type='password',
        password='teste123'
    )
    try:
        response = oauth_client.oauth_token().post()
    except Exception as erro:
        assert isinstance(erro, AssertionError)


@responses.activate
def test_autenticar_sem_password(crm_base_url, autenticador):
    oauth_client =  OauthClient(
        client_id='WvBxFof28HxjQjk0ryl94bAmpylKqie7kReNWHny',
        grant_type='password',
        username='testandinho@arbache.com'
    )
    try:
        response = oauth_client.oauth_token().post()
    except Exception as erro:
        assert isinstance(erro, AssertionError)
