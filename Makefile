.PHONY: db build run run-api stop clean logs \
        build-api test lint

# Start the DB container (for local use)
db:
	@echo "Starting DB container..."
	docker compose up -d migrate

# Build Docker image for local use (full stack)
build:
	@echo "Building full stack..."
	docker compose build

# Run only the API container (local)
run-api:
	@echo "Running API container..."
	docker compose up -d api

# Local development shortcut
run: db build run-api

# Stop and clean up
stop:
	docker compose down

clean:
	docker compose down -v

logs:
	docker compose logs -f

# ---------- CI Targets ----------

# ✅ Used by GitHub Actions: Build API Docker image
build-api:
	@echo "Building REST API Docker image..."
	docker build -t $(IMAGE_NAME):latest .

# ✅ Used by GitHub Actions: Run tests
test:
	@echo "Running tests with pytest..."
	pytest tests/

# ✅ Used by GitHub Actions: Lint code
lint:
	@echo "Running code linting with flake8..."
	flake8 app/ tests/

