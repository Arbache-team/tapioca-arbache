import responses
import status
from uuid import uuid4


@responses.activate
def test_retrieve_jogos(play_jogo_client, play_base_url):

    codigo = str(uuid4())

    responses.add(
        method=responses.GET,
        url=f"{play_base_url}/jogos-self/{codigo}/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = play_jogo_client.jogo(
        codigo=str(uuid4())
    ).get()

    assert response().status_code == status.HTTP_200_OK
