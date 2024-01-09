import pytest
from tapioca_arbache.exceptions import MissingUrlExeption


def test_adapter_especificando_url(perfil_adapter):
    api_params = {'url': 'https://teste.com.br'}
    api_root = perfil_adapter.get_api_root(api_params)
    assert api_root == api_params['url']


def test_adapter_sem_especificar_url(perfil_adapter):
    api_params = {}
    with pytest.raises(MissingUrlExeption):
        perfil_adapter.get_api_root(api_params)
