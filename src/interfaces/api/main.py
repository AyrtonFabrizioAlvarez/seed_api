from fastapi import FastAPI

app = FastAPI(title="NOMBRE DLE PROYECTO", version="VERSION DEL PROYECTO")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}
