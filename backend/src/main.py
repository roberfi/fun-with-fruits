from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.database import Base, engine
from src.fruits.router import router as fruits_router
from src.settings import get_settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fun with Fruits API",
    description="An API to have fun with fruits",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_settings().allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(fruits_router)
