import responses
import status
import uuid


@responses.activate
def test_retrieve_interface(interface_client, base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.GET,
        url=f"{base_url}/backend/perfil/{codigo}/interface/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = interface_client.interface(codigo=codigo).get()

    assert response().status_code == status.HTTP_200_OK


@responses.activate
def test_perfil_admin_retrieve_interface(interface_client, base_url):
    codigo = str(uuid.uuid4())
    responses.add(
        method=responses.GET,
        url=f"{base_url}/backend/admin/perfis/{codigo}/interface/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = interface_client.interface_admin(codigo=codigo).get()

    assert response().status_code == status.HTTP_200_OK
