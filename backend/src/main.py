from fastapi import FastAPI

from src.database import Base, engine
from src.fruits.router import router as fruits_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fun with Fruits API",
    description="An API to have fun with fruits",
    version="0.0.1",
)

app.include_router(fruits_router)
