.PHONY: lint lint-fix

lint:
	poetry run ruff check .

lint-fix:
	poetry run ruff check . --fix

.PHONY: migrations migrate

migrations:
ifndef m
	$(error m is not set. Usage: make migrations m="Your message")
endif
	alembic revision --autogenerate -m "$(m)"

migrate:
	alembic upgrade head
