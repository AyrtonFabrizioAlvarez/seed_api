# Instalacion

El repositorio esta pensado como un seed con herramientas basicas para desarrollar en un ambiente con las herramientas `Python`, `FastAPI`, `ruff`, `ty`, `lint`, `uvicorn`. Partimos de una estructura muy utilizada en `DDD` y `CleanArchitecture`

### Herramientas necesarias

- `mise` ([mise.jdx.dev](https://mise.jdx.dev/))
  - Administra herramientas de desarrollo y sus versiones, configurable en el archivo `mise.toml`
- `uv` ([docs.astral.sh/uv/getting-started/installation](https://docs.astral.sh/uv/getting-started/installation/))
  - Administra el entorno virtual y las dependencias

### Comandos:

```Shell
### Necesarios para correr la app
---------------------------------
mise install 	# Instalar herramientas de desarrollo
task sync		# Instalar dependencias


### Utiles para desarrollo
--------------------------
task dev 		# Levantar Servidor Web local de FastAPI:8000 - /src/interfaces/api/main.py
task test 		# Correr tests
task precommit  # Chequeos precommit (ruff, ty, lint)


### Cada una de estas Task esta definida dentro de Taskfile.yml
```
