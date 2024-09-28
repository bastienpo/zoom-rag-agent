.PHONY: run dev clean quality

run:
	uv run granian --interface asgi --workers 4 --threads 4 --loop uvloop app.main:app

dev:
	@echo "Starting development server..."
	@uv run granian --interface asgi --reload --loop uvloop --workers 1 app.main:app

clean:
	rm -rf **/*.pyc
	rm -rf **/__pycache__
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf ./lib

quality:
	ruff check .
	ruff format .

help:
	@echo "Usage:"
	@echo "  make run - Run the application"
	@echo "  make dev - Run the application in development mode"
	@echo "  make clean - Clean the project"
	@echo "  make quality - Check the code quality"
