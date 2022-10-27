test:
	pre-commit install
	poetry run pytest -vvv

lint:
	flake8
