import pytest


@pytest.fixture
def equipe():
    return {
        "total-registros": 1,
        "pagina-atual": 1,
        "total-paginas": 1,
        "registros": [
            {
                "codigo": "2110b7f9-be9e-43c4-9ec4-6b201f29ccdc",
                "equipe": "Equipe de Teste",
                "dono": "Willames Campos",
                "licencas": [
                    {
                        "disponiveis": 0,
                        "indisponiveis": 0
                    }
                ]
            }
        ]
    }
