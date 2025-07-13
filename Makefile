.PHONY: build-api test lint

build-api:
	@echo "Building REST API Docker image..."
	docker build -t dipakrasal2009/rest-api-webserver:latest .

test:
	@echo "Running tests with pytest..."
	PYTHONPATH=. pytest tests/

#lint:
#	@echo "Running code linting with flake8..."
#	flake8 app/ tests/
lint:
	@echo "Running code linting with flake8..."
	flake8 app/ tests/ --ignore=F401,F841,E302,E303,E305,E402,E501,W391,F811,E265

