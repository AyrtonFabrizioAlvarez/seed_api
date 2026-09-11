# Backend Seed

Base minima para construir una API con FastAPI y PostgreSQL. El repositorio usa
`uv` para Python y Docker Compose para ejecutar la API junto con la base de
datos.

## Requisitos

Para el flujo recomendado solo se necesita:

- Docker Engine
- Docker Compose

Para ejecutar la API directamente en la computadora tambien se necesita `uv`.

## Inicio rapido con Docker

Crear la configuracion local:

```bash
cp .env.example .env
```

Levantar la API y PostgreSQL:

```bash
docker compose up --build
```

La API queda disponible en:

- http://localhost:8000/health
- http://localhost:8000/health/ready
- http://localhost:8000/docs

El contenedor de PostgreSQL utiliza el volumen `postgres_data`. Para eliminar
tambien los datos persistidos:

```bash
docker compose down -v
```

## Migraciones

Alembic esta preparado para versionar el esquema. La migracion inicial es una
linea de base vacia, porque todavia no existe un modelo de negocio.

Con Docker:

```bash
docker compose run --rm api alembic upgrade head
```

Cuando se agregue el primer modelo:

```bash
docker compose run --rm api alembic revision --autogenerate -m "create entity"
docker compose run --rm api alembic upgrade head
```

## Desarrollo local

Este modo ejecuta la API en la computadora y PostgreSQL en Docker:

```bash
cp .env.example .env
docker compose up -d db
uv sync
uv run uvicorn src.interfaces.api.main:app --reload
```

En este caso la API usa `localhost:5432`. En el modo completamente dockerizado
Compose reemplaza el host por `db`, que es el nombre del servicio dentro de la
red de Docker.

No es necesario activar manualmente el entorno virtual. `uv run` utiliza el
entorno creado por `uv sync`.

## Verificaciones

```bash
uv run pytest
uv run ruff format --check .
uv run ruff check .
uv run ty check
```

Para agregar dependencias:

```bash
uv add nombre-del-paquete
uv add --dev nombre-del-paquete
```

Estos comandos actualizan `pyproject.toml` y `uv.lock`.

## Seeds

Todavia no hay datos de seed porque no existe un modelo de negocio. Cuando se
agregue el primer CRUD, el seed debera ser idempotente y ejecutarse como una
operacion separada:

```bash
docker compose run --rm api python -m src.infrastructure.database.seed
```
