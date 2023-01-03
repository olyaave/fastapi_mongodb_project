from fastapi import FastAPI

from app.server.routes.car import router as CarRouter

app = FastAPI()

app.include_router(CarRouter, tags=["Car"], prefix="/car")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to app!"}
