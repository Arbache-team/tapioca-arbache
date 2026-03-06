# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`tapioca-arbache` is a Python API client library for Arbache's services, built on top of the [tapioca-wrapper](https://github.com/vintasoftware/tapioca-wrapper) framework. It provides typed HTTP clients for CRM, Play, and Gestao APIs.

## Build & Development Commands

```bash
# Install dependencies (requires Poetry)
poetry install

# Run all tests
poetry run pytest -vvv

# Run a single test file
poetry run pytest tests/test_perfil_client.py -vvv

# Run a single test
poetry run pytest tests/test_perfil_client.py::test_perfil_get -vvv

# Lint
flake8

# Full test with pre-commit hooks
make test

# Lint via make
make lint
```

## Architecture

### Tapioca Wrapper Pattern

Every API client follows the same three-layer pattern:

1. **Resource Mapping** (`resource_mapping.py`) — Dictionaries defining API endpoints, their URL paths (with `{codigo}` placeholders for dynamic segments), and allowed HTTP methods.

2. **Adapter** (`tapioca_arbache.py`) — Classes extending `ArbacheAdapter` (which mixes `JSONAdapterMixin` + `TapiocaAdapter`). Each adapter binds a resource mapping and optionally overrides `prod_url`, `homolog_url`, `dev_url` for services hosted on different domains.

3. **Client** — Generated via `generate_wrapper_from_adapter(AdapterClass)`. Clients are instantiated with `access_token`, `perfil` (UUID), and optionally `ambiente` (`dev`/`homolog`) or a custom `url`.

### Service Domains

- **CRM** (`crm.arbache.com.br`) — Perfil, Oauth, Licenca, Jogo, Equipe, CrmMidia, Interface
- **Play** (`play-api.arbache.dev.br`) — JogoSelf, PlayMidia, ResultadoJogo, PlaySubdominio, PlayJogosSubdominio
- **Gestao** (`gestao.arbache.dev.br`) — Relatorio

### Adding a New Client

1. Add endpoint mapping dict in `resource_mapping.py`
2. Create an adapter class in `tapioca_arbache.py` (extend `ArbacheAdapter`, set `resource_mapping`, override URLs if non-CRM service)
3. Generate client: `NewClient = generate_wrapper_from_adapter(NewAdapter)`
4. Export in `__init__.py`

## Testing

Tests use `responses` library to mock HTTP calls with `@responses.activate` decorator. Fixtures are in `tests/conftest.py` and `tests/fixtures/`. Each test mocks an endpoint, calls the client method, and asserts status code and response data.

## Linting

- Flake8 with `max-line-length = 100`
- Excludes: `__init__.py`, `fixtures/`, `local/`

## Pre-commit Hooks

Configured in `.pre-commit-config.yaml`: YAML/JSON checks, trailing whitespace, end-of-file fixer, debug statements, and **no direct commits to `main`**.
