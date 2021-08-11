import pytest
import uuid

from tapioca_arbache.tapioca_arbache import PerfilAdapter
from tapioca_arbache import PerfilClient, LicencaClient, OauthClient


pytest_plugins = [
    "tests.fixtures.perfil",
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
def oauth_client():
    return OauthClient(
        client_id='WvBxFof28HxjQjk0ryl94bAmpylKqie7kReNWHny',
        grant_type='password',
        username='testandinho@arbache.com',
        password='teste123'
    )

@pytest.fixture
def licenca_client():
    return LicencaClient(
        access_token="xoBS2UF8HH6jOpRdQfytvr036XkWY7",
        perfil=str(uuid.uuid4())
    )
