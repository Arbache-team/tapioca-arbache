import responses
import status
import uuid


@responses.activate
def test_criar_subdominio(
    play_subdominio_client, play_base_url, response_OK, request_body
):

    responses.add(
        method=responses.POST,
        url=f"{play_base_url}/subdominios/",
        status=status.HTTP_200_OK,
        json=response_OK
    )

    response = play_subdominio_client.subdominios().post(data=request_body)

    assert response().status_code == status.HTTP_200_OK


@responses.activate
def test_atualizar_subdominio(play_subdominio_client, play_base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.PATCH,
        url=f"{play_base_url}/subdominios/{codigo}/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = play_subdominio_client.subdominio(codigo=codigo).patch()

    assert response().status_code == status.HTTP_200_OK


@responses.activate
def test_retrieve_subdominio(
    play_subdominio_client, play_base_url, response_OK
):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.GET,
        url=f"{play_base_url}/subdominios/{codigo}/",
        status=status.HTTP_200_OK,
        json=response_OK
    )

    response = play_subdominio_client.subdominio(codigo=codigo).get()

    assert response().status_code == status.HTTP_200_OK
