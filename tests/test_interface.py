import responses
import status
import uuid


@responses.activate
def test_retrieve_interface(interface_client, crm_base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.GET,
        url=f"{crm_base_url}/backend/perfis/configuracoes/{codigo}/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = interface_client.interface(codigo=codigo).get()

    assert response().status_code == status.HTTP_200_OK
