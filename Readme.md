# Arbache Tapioca Clients
<div align="right">Ultima atualização: 29/07/2021</div>

## Clients
Python clients para acessar os recursos das apis da arbache

## Como usar
```
# pip install {}
```

Para instânciar um client basta informar o `access_token` e o `perfil` e o `ambiente`. Caso o parâmetro ambiente seja omitido, as requisições irão para produção.
```
perfil_client = PerfilClien(
    access_token='xoBS2UF8HH6jOpRdQfytvr036XkWY7',
    perfil='18e42445-a1ee-407c-a1a5-84739c4bc9da',
    ambiente='dev'
)
```

Os ambientes disponíveis são `dev` e `homolog`


