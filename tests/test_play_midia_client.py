import responses
import status


@responses.activate
def test_list_midias(play_midia_client, base_url):

    responses.add(
        method=responses.GET,
        url=f"{base_url}/midias/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = play_midia_client.midias().get()

    assert response().status_code == status.HTTP_200_OK
