from fastapi import APIRouter

from src.fruits.services import FruitsDb
from src.fruits.schemas import Fruit, FruitCreate, FruitUpdate

router = APIRouter()


fruits_db = FruitsDb()


@router.get("/fruits", tags=["fruits"])
async def read_fruits() -> list[Fruit]:
    return fruits_db.get_fruits()


@router.get("/fruits/{fruit_id}", tags=["fruits"])
async def read_fruit(fruit_id: int) -> Fruit:
    return fruits_db.get_fruit(fruit_id)


@router.post("/fruits", tags=["fruits"])
async def create_fruit(fruit: FruitCreate) -> Fruit:
    return fruits_db.add_fruit(fruit)


@router.put("/fruits/{fruit_id}", tags=["fruits"])
async def update_fruit(fruit_id: int, fruit: FruitUpdate) -> Fruit:
    return fruits_db.update_fruit(fruit_id, fruit)


@router.delete("/fruits/{fruit_id}", tags=["fruits"])
async def delete_fruit(fruit_id: int) -> None:
    return fruits_db.delete_fruit(fruit_id)
