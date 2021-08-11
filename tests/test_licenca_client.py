import responses
import status
import uuid


@responses.activate
def test_retrieve_licenca(licenca_client, crm_base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.GET,
        url=f"{crm_base_url}/backend/licencas/{codigo}",
        status=status.HTTP_200_OK,
        json={}
    )

    response = licenca_client.licenca(codigo=codigo).get()

    assert response().status_code == status.HTTP_200_OK


@responses.activate
def test_retrieve_licenca_sem_codigo(licenca_client, crm_base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.GET,
        url=f"{crm_base_url}/backend/licencas/{codigo}",
        status=status.HTTP_200_OK,
        json={}
    )

    response = licenca_client.licenca(codigo=codigo).get()

    assert response().status_code == status.HTTP_200_OK
