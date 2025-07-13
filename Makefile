.PHONY: build-api test lint

build-api:
	@echo "Building REST API Docker image..."
	docker build -t $(IMAGE_NAME):latest .

test:
	@echo "Running tests with pytest..."
	pytest tests/

lint:
	@echo "Running code linting with flake8..."
	flake8 app/ tests/

