import responses
import status


@responses.activate
def test_perfil_get(perfil_client, base_url, perfil):
    responses.add(
        method=responses.GET,
        url=f"{base_url}/backend/perfil/",
        status=status.HTTP_200_OK,
        json=perfil,
    )

    response = perfil_client.perfis().get()

    assert response().status_code == status.HTTP_200_OK
    assert response().data == perfil
