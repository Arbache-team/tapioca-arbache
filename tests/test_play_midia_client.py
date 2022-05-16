import responses
import status


@responses.activate
def test_list_midias(play_midia_client, play_base_url):

    responses.add(
        method=responses.GET,
        url=f"{play_base_url}/midias/",
        status=status.HTTP_200_OK,
        json={}
    )

    response = play_midia_client.midias().get()

    assert response().status_code == status.HTTP_200_OK
