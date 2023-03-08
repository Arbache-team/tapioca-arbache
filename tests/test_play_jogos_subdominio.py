import responses
import status
import uuid


@responses.activate
def test_criar_subdominio(
    play_jogos_subdominio_client, play_base_url, response_OK, request_body
):

    responses.add(
        method=responses.POST,
        url=f"{play_base_url}/jogos-subdominios/",
        status=status.HTTP_200_OK,
        json=response_OK
    )

    response = play_jogos_subdominio_client.jogos().post(data=request_body)

    assert response().status_code == status.HTTP_200_OK


@responses.activate
def test_atualizar_jogosubdominio(play_jogos_subdominio_client, play_base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.PATCH,
        url=f"{play_base_url}/jogos-subdominios/{codigo}/",
        status=status.HTTP_200_OK,
        json={
            'preco': 10.00
        }
    )

    response = play_jogos_subdominio_client.jogo(codigo=codigo).patch()

    assert response().status_code == status.HTTP_200_OK
