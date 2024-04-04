from fastapi import FastAPI
from app.utilities.db import Base, engine
from app.routers.auth import auth

sermov_api_description = """
This is the Sermov API.
"""

app = FastAPI(
    title="Sermov API",
    description=sermov_api_description,
    version="0.1.0",
)
Base.metadata.create_all(bind=engine)

import debugpy
debugpy.listen(("0.0.0.0", 5678))

app.include_router(
    auth.router,
    prefix="/v1/auth",
    tags=["auth"]
)

@app.get("/")
async def root() -> dict[str, str]:
    return {"Hello": "World"}