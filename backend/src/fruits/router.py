from fastapi import APIRouter, Depends

from src.database import get_db
from src.fruits import service
from src.fruits.schemas import Fruit, FruitCreate, FruitUpdate
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/fruits", tags=["fruits"])
async def read_fruits(db: Session = Depends(get_db)) -> list[Fruit]:
    return service.get_fruits(db)


@router.get("/fruits/{fruit_id}", tags=["fruits"])
async def read_fruit(fruit_id: int, db: Session = Depends(get_db)) -> Fruit:
    return service.get_fruit(fruit_id, db)


@router.post("/fruits", tags=["fruits"], status_code=201)
async def create_fruit(fruit: FruitCreate, db: Session = Depends(get_db)) -> Fruit:
    return service.add_fruit(fruit, db)


@router.put("/fruits/{fruit_id}", tags=["fruits"])
async def update_fruit(
    fruit_id: int, fruit: FruitUpdate, db: Session = Depends(get_db)
) -> Fruit:
    return service.update_fruit(fruit_id, fruit, db)


@router.delete("/fruits/{fruit_id}", tags=["fruits"], status_code=204)
async def delete_fruit(fruit_id: int, db: Session = Depends(get_db)) -> None:
    service.delete_fruit(fruit_id, db)
