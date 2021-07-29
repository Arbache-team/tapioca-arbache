import pytest


@pytest.fixture
def perfil():
    return {
        "total-registros": 2,
        "pagina-atual": 1,
        "total-paginas": 1,
        "registros": [
            {
                "nome": "Testandinho Albuquerque",
                "email": "testandinho@arbache.com",
                "level": 6,
                "pk": "0b3b47f7-6e36-44c0-97f5-7b54215c4c1e",
                "perfil": "Revenda",
                "documento": "12345678910",
                "detalhes": None,
                "dono": True
            },
            {
                "nome": "Testandinho Albuquerque",
                "email": "testandinho@arbache.com",
                "level": 3,
                "pk": "18e42445-a1ee-407c-a1a5-84739c4bc9da",
                "perfil": "Perfil Profissional",
                "documento": "12345678910",
                "detalhes": None,
                "dono": True
            }
        ]
    }