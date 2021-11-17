CRM_PERFIL_ENDPOINT = {
    "perfis": {
        "resource": "backend/perfis/",
        "methods": ["GET"],
    }
}
CRM_OAUTH = {
    "oauth_token": {
        "resource": "backend/oauth-token/",
        "methods": ["POST"],
    }
}
CRM_LICENCA_ENDPOINT = {
    "licencas-list": {
        "resource": "backend/licencas/",
        "methods": ["GET"],
    },
    "licenca": {
        "resource": "backend/licencas/{codigo}/",
        "methods": ["GET"],
    }
}
JOGO_SELF = {
    "jogos": {
        "resource": "/jogos-self/",
        "methods": ["GET"],
    }
}
RELATORIOS = {
    "relatorios": {
        "resource": "/relatorios/",
        "methods": ["GET", "POST"],
    }
}
CRM_JOGO_ENDPOINT = {
    "jogos-list" : {
        "resource": "backend/jogos/",
        "methods": ["GET"]
    },
    "jogos" : {
        "resource": "backend/jogos/{codigo}/",
        "methods": ["GET, PATCH"]
    }
}
