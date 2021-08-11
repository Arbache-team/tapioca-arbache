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
