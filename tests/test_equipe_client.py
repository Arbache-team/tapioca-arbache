import responses
import status
import uuid


@responses.activate
def test_list_equipes(equipe_client, base_url):

    responses.add(
        method=responses.GET,
        url=f"{base_url}/backend/equipes/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = equipe_client.equipes().get()

    assert response().status_code == status.HTTP_200_OK


@responses.activate
def test_retrieve_equipe(equipe_client, base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.GET,
        url=f"{base_url}/backend/equipes/{codigo}/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = equipe_client.equipe(codigo=codigo).get()

    assert response().status_code == status.HTTP_200_OK
