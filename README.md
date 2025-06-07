# Build an Analytics API using FastAPI + Time-series Postgres

Own your data pipeline! 

Start by building an Analytics API service with Python, FastAPI, and Time-series Postgres with TimescaleDB



## Docker

- `docker build -t analytic-api -f Dockerfile.web .`
- `docker run analytic-api `

becomes

- `docker compose up --watch`
- `docker compose down` or `docker compose down -v` (to remove volumes)
- `docker compose run app /bin/bash` or `docker compose run app python` 