ALL_PACKAGES := src tests

.PHONY: reformat lint api

lint:
	poetry run black --check --diff $(ALL_PACKAGES) &
	poetry run isort --check --diff $(ALL_PACKAGES) &
	poetry run flake8 $(ALL_PACKAGES) &
	poetry run mypy .

reformat:
	poetry run isort $(ALL_PACKAGES)
	poetry run black $(ALL_PACKAGES)

api:
	poetry run uvicorn hipotecas_calculador.api.fastapi_app:app --reload