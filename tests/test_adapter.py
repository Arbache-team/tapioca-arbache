def test_adapter_dev(perfil_adapter):
    api_params = {'ambiente': 'dev'}
    api_root = perfil_adapter.get_api_root(api_params)
    assert api_root == perfil_adapter.dev_url

def test_adapter_homolog(perfil_adapter):
    api_params = {'ambiente': 'homolog'}
    api_root = perfil_adapter.get_api_root(api_params)
    assert api_root == perfil_adapter.homolog_url

def test_adapter(perfil_adapter):
    api_params = {}
    api_root = perfil_adapter.get_api_root(api_params)
    assert api_root == perfil_adapter.prod_url
