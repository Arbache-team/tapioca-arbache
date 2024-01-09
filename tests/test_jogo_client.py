import responses
import status
import uuid


@responses.activate
def test_retrieve_jogo(jogo_client, base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.GET,
        url=f"{base_url}/backend/jogos/{codigo}/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = jogo_client.jogo(codigo=codigo).get()

    assert response().status_code == status.HTTP_200_OK
