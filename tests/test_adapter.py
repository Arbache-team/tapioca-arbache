def test_adapter_especificando_url(perfil_adapter):
    api_params = {'url': 'https://teste.com.br'}
    api_root = perfil_adapter.get_api_root(api_params)
    assert api_root == api_params['url']
