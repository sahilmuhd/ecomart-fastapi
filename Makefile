# Makefile for EcoMart FastAPI Project

.PHONY: help install run test docker-build docker-compose-up docker-compose-down

help: 
	@echo "Makefile commands:"
	@echo "  install            Install dependencies"
	@echo "  run                Run the FastAPI application"
	@echo "  test               Run tests"
	@echo "  docker-build       Build the Docker image"
	@echo "  docker-compose-up  Start the application with Docker Compose"
	@echo "  docker-compose-down Stop the application with Docker Compose"

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest tests/

docker-build:
	docker build -t ecomart-fastapi .

docker-compose-up:
	docker-compose up --build

docker-compose-down:
	docker-compose down