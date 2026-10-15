<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:0d0221,50:7b2ff7,100:00f0ff&text=EcoMart%20API&fontColor=00f0ff&fontSize=48&fontAlignY=38&desc=Multi-tenant%20e-commerce%20backend%20built%20with%20FastAPI&descAlignY=58&descSize=16&animation=fadeIn" alt="EcoMart API"/>

<img src="https://img.shields.io/badge/FastAPI-0d0221?style=for-the-badge&logo=fastapi&logoColor=00f0ff"/>
<img src="https://img.shields.io/badge/Python-0d0221?style=for-the-badge&logo=python&logoColor=7b2ff7"/>
<img src="https://img.shields.io/badge/PostgreSQL-0d0221?style=for-the-badge&logo=postgresql&logoColor=ff2a6d"/>
<img src="https://img.shields.io/badge/SQLAlchemy-0d0221?style=for-the-badge&logo=sqlalchemy&logoColor=00f0ff"/>
<img src="https://img.shields.io/badge/Redis-0d0221?style=for-the-badge&logo=redis&logoColor=7b2ff7"/>
<img src="https://img.shields.io/badge/Celery-0d0221?style=for-the-badge&logo=celery&logoColor=ff2a6d"/>
<img src="https://img.shields.io/badge/Docker-0d0221?style=for-the-badge&logo=docker&logoColor=00f0ff"/>
<img src="https://img.shields.io/badge/Pytest-0d0221?style=for-the-badge&logo=pytest&logoColor=7b2ff7"/>

</div>

## // OVERVIEW

EcoMart is a multi-tenant e-commerce API scaffold built with FastAPI. It sets up routers, models, schemas, services, a tenant-context middleware, Redis and Celery wiring, and a Docker Compose environment for stores, products, inventory and orders.

> Status: early-stage scaffold. Some routers (for example inventory and stores) import modules that are not yet in the repo, so treat it as a work in progress.

## // FEATURES

- Versioned API under `/api/v1` with routers for auth, stores, products, inventory and orders
- Tenant context middleware that reads the `X-Tenant-ID` request header and rejects requests without it
- SQLAlchemy models for users, tenants, stores, products, inventory and orders, with an Alembic folder for migrations
- Celery app and background tasks (`sync_inventory`, `process_order`)
- Redis client module for caching
- Password hashing dependency (`passlib[bcrypt]`) and Pydantic schemas
- Pytest suite scaffold (health, products, orders)
- Dockerfile, Celery Dockerfile and `docker-compose.yml` (web, PostgreSQL, Redis, Celery)

## // TECH_STACK

| Layer | Tools |
| --- | --- |
| API | FastAPI, Uvicorn, Pydantic |
| Database | PostgreSQL, SQLAlchemy, Alembic, asyncpg |
| Cache and queue | Redis, Celery |
| Testing | Pytest, pytest-asyncio, httpx |
| Tooling | Docker, Docker Compose, Makefile |

## // GETTING_STARTED

```bash
git clone https://github.com/sahilmuhd/ecomart-fastapi.git
cd ecomart-fastapi

# configure environment (see .env.example for the variable names)
cp .env.example .env

# option 1: Docker (web, PostgreSQL, Redis, Celery)
docker-compose up --build

# option 2: local
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# run tests
pytest tests/
```

Environment variables listed in `.env.example`: `DATABASE_URL`, `REDIS_URL`, `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND`, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CORS_ORIGINS`, `TENANT_MODEL`, `DEFAULT_TENANT`.

## // PROJECT_STRUCTURE

```
ecomart-fastapi
├── app
│   ├── main.py            # FastAPI app, CORS, tenant middleware, routers
│   ├── api/v1             # routers (auth, stores, products, inventory, orders) and deps
│   ├── core               # config and Celery app
│   ├── db                 # base, session, models
│   ├── schemas            # Pydantic schemas
│   ├── services           # auth, product, order services
│   ├── tasks              # Celery background jobs
│   ├── cache              # Redis client
│   ├── middleware         # tenant context middleware
│   └── utils              # pagination, exceptions
├── alembic/versions
├── tests
├── docker/celery
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── requirements.txt
```

## // AUTHOR

Sahil, [github.com/sahilmuhd](https://github.com/sahilmuhd)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:00f0ff,50:7b2ff7,100:0d0221&section=footer" alt="footer"/>

Built by [Sahil](https://github.com/sahilmuhd) · [sahilmuhd.com](https://sahilmuhd.com)

</div>
