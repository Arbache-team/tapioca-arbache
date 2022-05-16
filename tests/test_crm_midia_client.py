import responses
import status


@responses.activate
def test_list_midias(crm_midia_client, crm_base_url):

    responses.add(
        method=responses.GET,
        url=f"{crm_base_url}/backend/midias/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = crm_midia_client.midias().get()

    assert response().status_code == status.HTTP_200_OK
