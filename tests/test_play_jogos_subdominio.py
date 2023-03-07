import responses
import status


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
