# Configuration
SERVER_PORT=8000

# Load environment variables from .env file if it exists
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Targets for common tasks
.PHONY: install setup test lint serve start stop pyclean migrate-local

# Install dependencies using pip
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Apply Django migrations locally
migrate-local:
	python manage.py makemigrations
	python manage.py migrate

# Run tests
test: migrate-local
	python manage.py test

# Run tests with coverage report
test-with-coverage: migrate-local
	pytest src/tests --cov=src/app --cov-report term-missing:skip-covered --cov-report xml:.test-reports/coverage.xml --junitxml=.test-reports/test-run.xml

# Lint the codebase
lint:
	pre-commit run --all-files

# Lint only changed files
lint-changed:
	git status --porcelain | egrep -v '^(D |RM|R )' | cut -b 4- | xargs pre-commit run --files

# Serve the application locally
serve:
	python manage.py runserver 0.0.0.0:$(SERVER_PORT)

# Docker operations using docker-compose
start:
	docker-compose up -d

stop:
	docker-compose down

# Clean Python cache files and artifacts
pyclean:
	find . -name "*.py[co]" -o -name __pycache__ -exec rm -rf {} +

# Default target (set to serve the application)
default: serve