from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.common.schemas import HTTPError
from src.database import get_db
from src.fruits import service
from src.fruits.schemas import Fruit, FruitCreate, FruitUpdate

router = APIRouter()


@router.get(
    "/fruits",
    tags=["fruits"],
    description="Retrieve a list of all fruits.",
)
async def read_fruits(db: Session = Depends(get_db)) -> list[Fruit]:
    return service.get_fruits(db)


@router.get(
    "/fruits/{fruit_id}",
    tags=["fruits"],
    responses={404: {"model": HTTPError}},
    description="Retrieve a specific fruit by its ID.",
)
async def read_fruit(fruit_id: int, db: Session = Depends(get_db)) -> Fruit:
    return service.get_fruit(fruit_id, db)


@router.post(
    "/fruits",
    tags=["fruits"],
    status_code=201,
    description="Create a new fruit.",
)
async def create_fruit(fruit: FruitCreate, db: Session = Depends(get_db)) -> Fruit:
    return service.add_fruit(fruit, db)


@router.put(
    "/fruits/{fruit_id}",
    tags=["fruits"],
    responses={404: {"model": HTTPError}},
    description="Update an existing fruit by its ID.",
)
async def update_fruit(fruit_id: int, fruit: FruitUpdate, db: Session = Depends(get_db)) -> Fruit:
    return service.update_fruit(fruit_id, fruit, db)


@router.delete(
    "/fruits/{fruit_id}",
    tags=["fruits"],
    status_code=204,
    responses={404: {"model": HTTPError}},
    description="Delete a fruit by its ID.",
)
async def delete_fruit(fruit_id: int, db: Session = Depends(get_db)) -> None:
    service.delete_fruit(fruit_id, db)
