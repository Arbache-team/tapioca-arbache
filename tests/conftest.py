import pytest
import uuid

from tapioca_arbache.tapioca_arbache import PerfilAdapter
from tapioca_arbache import (
    PerfilClient, LicencaClient, JogoClient,
    EquipeClient, CrmMidiaClient, PlayMidiaClient,
    InterfaceClient, RelatorioClient
)


pytest_plugins = [
    "tests.fixtures.perfil",
    "tests.fixtures.relatorios"
]


@pytest.fixture
def crm_base_url():
    return "https://crm.arbache.com.br"


@pytest.fixture
def play_base_url():
    return "https://play-api-homolog.arbache.dev.br"


@pytest.fixture
def gestao_base_url():
    return "https://gestao.arbache.dev.br"


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
def relatorio_client():
    return RelatorioClient(
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


@pytest.fixture
def play_midia_client():
    return PlayMidiaClient(
        access_token="xoBS2UF8HH6jOpRdQfytvr036XkWY7",
        perfil=str(uuid.uuid4()),
        url='https://play-api-homolog.arbache.dev.br'
    )


@pytest.fixture
def interface_client():
    return InterfaceClient(
        access_token="xoBS2UF8HH6jOpRdQfytvr036XkWY7",
        perfil=str(uuid.uuid4()),
    )


@pytest.fixture
def crm_midia_client():
    return CrmMidiaClient(
        access_token="xoBS2UF8HH6jOpRdQfytvr036XkWY7",
        perfil=str(uuid.uuid4()),
    )
