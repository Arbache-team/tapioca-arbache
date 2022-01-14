import pytest
import uuid

from tapioca_arbache.tapioca_arbache import PerfilAdapter
from tapioca_arbache import (
    PerfilClient, LicencaClient, OauthClient, JogoClient,
    EquipeClient
)


pytest_plugins = [
    "tests.fixtures.perfil",
    "tests.fixtures.equipe",
]


@pytest.fixture
def crm_base_url():
    return "https://crm.arbache.com.br"

@pytest.fixture
def perfil_adapter():
    return PerfilAdapter()

@pytest.fixture
def perfil_client():
    return PerfilClient(
        access_token="xoBS2UF8HH6jOpRdQfytvr036XkWY7",
        perfil=str(uuid.uuid4())
    )

@pytest.fixture
def licenca_client():
    return LicencaClient(
        access_token="xoBS2UF8HH6jOpRdQfytvr036XkWY7",
        perfil=str(uuid.uuid4())
    )

@pytest.fixture
def jogo_client():
    return JogoClient(
        access_token="xoBS2UF8HH6jOpRdQfytvr036XkWY7",
        perfil=str(uuid.uuid4())
    )


@pytest.fixture
def equipe_client():
    return EquipeClient(
        access_token="xoBS2UF8HH6jOpRdQfytvr036XkWY7",
        perfil=str(uuid.uuid4())
    )
