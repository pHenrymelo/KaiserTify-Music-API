deploy:
	uvicorn main:app --reload --app-dir src

test:
	pytest --cov=src --cov-report=term-missing