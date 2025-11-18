# EcoMart API

EcoMart is a multi-tenant e-commerce platform designed to facilitate store management, product catalog management, inventory management, and order processing. This project leverages FastAPI for building the API, Redis for caching, and Celery for background job processing. It is containerized using Docker for easy deployment and scalability.

## Features

- **Multi-Tenant Architecture**: Supports multiple vendors with isolated data.
- **Store Management**: Vendors can create and manage their stores.
- **Product Catalog**: Manage products with features to add, update, and retrieve product information.
- **Inventory Management**: Track product stock levels efficiently.
- **Order Processing**: Create and manage customer orders seamlessly.
- **Background Jobs**: Utilize Celery for handling background tasks such as sending emails and syncing inventory.
- **Caching**: Improve performance with Redis caching.

## Project Structure

```
ecomart-fastapi
├── app
│   ├── main.py
│   ├── api
│   │   └── v1
│   │       ├── routers
│   │       │   ├── auth.py
│   │       │   ├── stores.py
│   │       │   ├── products.py
│   │       │   ├── inventory.py
│   │       │   └── orders.py
│   │       └── deps.py
│   ├── core
│   │   ├── config.py
│   │   └── celery_app.py
│   ├── db
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models
│   │       ├── user.py
│   │       ├── tenant.py
│   │       ├── store.py
│   │       ├── product.py
│   │       ├── inventory.py
│   │       └── order.py
│   ├── schemas
│   │   ├── user.py
│   │   ├── tenant.py
│   │   ├── store.py
│   │   ├── product.py
│   │   └── order.py
│   ├── services
│   │   ├── auth_service.py
│   │   ├── product_service.py
│   │   └── order_service.py
│   ├── tasks
│   │   ├── __init__.py
│   │   └── background_jobs.py
│   ├── cache
│   │   └── redis_client.py
│   ├── middleware
│   │   └── tenant_middleware.py
│   └── utils
│       ├── pagination.py
│       └── exceptions.py
├── alembic
│   └── versions
├── tests
│   ├── conftest.py
│   ├── test_health.py
│   └── api
│       ├── test_products.py
│       └── test_orders.py
├── docker
│   └── celery
│       └── Dockerfile
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
├── Makefile
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker and Docker Compose
- Redis
- PostgreSQL (or your preferred database)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ecomart-fastapi.git
   cd ecomart-fastapi
   ```

2. Create a `.env` file based on the `.env.example` file and configure your environment variables.

3. Build and run the application using Docker:
   ```
   docker-compose up --build
   ```

### Running Tests

To run the tests, use the following command:
```
pytest
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.