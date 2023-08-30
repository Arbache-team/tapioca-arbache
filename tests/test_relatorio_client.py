import json
import responses
import status
import pytest
from tapioca.exceptions import ClientError


@responses.activate
def test_response_OK_relatorio(
    relatorio_client, gestao_base_url, response_OK, request_body
):
    responses.add(
        method=responses.POST,
        url=f"{gestao_base_url}/backend/relatorios/",
        status=status.HTTP_200_OK,
        json=response_OK
    )

    response = relatorio_client.relatorios().post(data=request_body)

    assert response().status_code == status.HTTP_200_OK


@responses.activate
def test_response_BAD_REQUEST(
    relatorio_client, gestao_base_url, response_BAD_REQUEST, request_body
):
    responses.add(
        method=responses.POST,
        url=f"{gestao_base_url}/backend/relatorios/",
        status=status.HTTP_400_BAD_REQUEST,
        json=response_BAD_REQUEST
    )

    with pytest.raises(ClientError) as erro:
        relatorio_client.relatorios().post(data=request_body)

    assert erro.value.status_code == status.HTTP_400_BAD_REQUEST
    assert all(
        key in response_BAD_REQUEST.keys() for key in erro.value.args[0]['response_body'].keys() # noqa
    )
    assert all(
        key in request_body.keys() for key in erro.value.args[0]['request_body'].keys() # noqa
    )
