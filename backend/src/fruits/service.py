from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.fruits.models import DBFruit
from src.fruits.schemas import Fruit, FruitCreate, FruitUpdate


def get_fruits(db: Session) -> list[Fruit]:
    return [Fruit(**db_fruit.__dict__) for db_fruit in db.query(DBFruit).all()]


def get_fruit(fruit_id: int, db: Session) -> Fruit:
    db_fruit = db.query(DBFruit).filter(DBFruit.id == fruit_id).one_or_none()

    if not db_fruit:
        raise HTTPException(status_code=404, detail=f"Fruit with id {fruit_id} not found")

    return Fruit(**db_fruit.__dict__)


def add_fruit(fruit: FruitCreate, db: Session) -> Fruit:
    db_fruit = DBFruit(**fruit.model_dump())
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return Fruit(**db_fruit.__dict__)


def update_fruit(fruit_id: int, fruit: FruitUpdate, db: Session) -> Fruit:
    db_fruit = db.query(DBFruit).filter(DBFruit.id == fruit_id).one_or_none()

    if not db_fruit:
        raise HTTPException(status_code=404, detail=f"Fruit with id {fruit_id} not found")

    for field, value in fruit.model_dump(exclude_none=True).items():
        setattr(db_fruit, field, value)

    db.commit()
    db.refresh(db_fruit)

    return Fruit(**db_fruit.__dict__)


def delete_fruit(fruit_id: int, db: Session) -> None:
    db_fruit = db.query(DBFruit).filter(DBFruit.id == fruit_id).one_or_none()

    if db_fruit is None:
        raise HTTPException(status_code=404, detail=f"Fruit with id {fruit_id} not found")

    db.delete(db_fruit)
    db.commit()
