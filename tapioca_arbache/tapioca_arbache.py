from tapioca import (
    JSONAdapterMixin, TapiocaAdapter, generate_wrapper_from_adapter
)
from requests_oauthlib import OAuth2
from tapioca_arbache.resource_mapping import (
    CRM_PERFIL_ENDPOINT, CRM_AUTENTICADOR
)


class ArbacheAdapter(JSONAdapterMixin, TapiocaAdapter):

    def get_api_root(self, api_params, **kwargs):
        if api_params.get('ambiente', '').lower() == 'dev':
            return self.dev_url
        elif api_params.get('ambiente', '').lower() == 'homolog':
            return self.homolog_url
        else:
            return self.prod_url

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(ArbacheAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )

        assert 'perfil' in api_params, ('Obrigatorio passar o perfil requisitante')

        params['auth'] = OAuth2(
            api_params.get('client_id'),
            token={
                'access_token': api_params.get('access_token'),
                'token_type': 'Bearer'
            }
        )

        if not params.get('params', False):
            params['params'] = {}

        params['params']['perfil'] = api_params['perfil']

        return params

    def get_iterator_list(self, response_data):
        return response_data['registros']

    def get_iterator_next_request_kwargs(
        self, iterator_request_kwargs, response_data, response
    ):
        pagina_atual = iterator_request_kwargs['params'].get('pagina', None)
        if pagina_atual is None:
            iterator_request_kwargs['params']['pagina'] = 2
        else:
            iterator_request_kwargs['params']['pagina'] =  pagina_atual + 1

        return iterator_request_kwargs


class ArbacheOauthAdapter(ArbacheAdapter):

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(ArbacheAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )

        return params


class PerfilAdapter(ArbacheAdapter):
    prod_url = 'https://crm.arbache.com.br'
    homolog_url = 'https://crm-homolog.dev.br'
    dev_url = 'http://127.0.0.1:8000'
    resource_mapping = CRM_PERFIL_ENDPOINT


class AutenticadorAdapter(ArbacheOauthAdapter):
    prod_url = 'https://crm.arbache.com.br'
    homolog_url = 'https://crm-homolog.dev.br'
    dev_url = 'http://127.0.0.1:8000'
    resource_mapping = CRM_AUTENTICADOR


PerfilClient = generate_wrapper_from_adapter(PerfilAdapter)
AutenticadorClient = generate_wrapper_from_adapter(AutenticadorAdapter)