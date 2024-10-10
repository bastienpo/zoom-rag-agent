.PHONY: run dev clean quality

run:
	uv run granian --interface asgi --workers 4 --threads 4 --loop uvloop app.main:app

dev:
	@echo "Starting development server..."
	@uv run granian --port 4000 --interface asgi --reload --loop uvloop --workers 1 --log app.main:app

clean:
	@echo "Cleaning the project files..."
	rm -rf **/*.pyc **/__pycache__
	rm -rf .pytest_cache
	ruff clean

check:
	ruff check --config pyproject.toml
	ruff format --check --config pyproject.toml 

fix:
	ruff format . --config pyproject.toml
	ruff check . --select I --fix --unsafe-fixes --config pyproject.toml

help:
	@echo "Usage:"
	@echo "  make run - Run the application"
	@echo "  make dev - Run the application in development mode"
	@echo "  make check - Check the code quality"
	@echo "  make fix - Fix the code quality"
	@echo "  make clean - Clean the project files"
