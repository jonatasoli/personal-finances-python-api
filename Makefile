.PHONY: install shell format lint test sec export configs run coverage

install:
	@poetry install

shell:
	@poetry shell

format:
	@isort .
	@blue .

lint:
	@blue . --check
	@isort . --check
	@prospector --no-autodetect

test:
	@pytest -s -m 'not api'

sec:
	@safety check

export:
	@poetry export -f requirements.txt --output requirements.txt

configs:
	dynaconf -i src.config.settings list

coverage:
	coverage run --source=src -m pytest

run:
	@poetry run uvicorn src.main:create_app --factory --host 0.0.0.0 --port 8000 --reload
