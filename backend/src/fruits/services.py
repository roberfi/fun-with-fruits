# Temporary in-memory database
from fastapi import HTTPException
from src.fruits.schemas import Fruit, FruitCreate, FruitUpdate


class FruitsDb:
    def __init__(self) -> None:
        self.__next_id = 1
        self.__fruits: list[Fruit] = []

    def add_fruit(self, fruit: FruitCreate) -> Fruit:
        self.__fruits.append(
            new_fruit := Fruit(id=self.__next_id, **fruit.model_dump())
        )
        self.__next_id += 1
        return new_fruit

    def get_fruits(self) -> list[Fruit]:
        return self.__fruits

    def get_fruit(self, fruit_id: int) -> Fruit:
        for fruit in self.__fruits:
            if fruit.id == fruit_id:
                return fruit

        raise HTTPException(
            status_code=404, detail=f"Fruit with id {fruit_id} not found"
        )

    def update_fruit(self, fruit_id: int, fruit: FruitUpdate) -> Fruit:
        for index, _fruit in enumerate(self.__fruits):
            if _fruit.id == fruit_id:
                self.__fruits[index] = _fruit.model_copy(
                    update=fruit.model_dump(exclude_unset=True)
                )
                return self.__fruits[index]

        raise HTTPException(
            status_code=404, detail=f"Fruit with id {fruit_id} not found"
        )

    def delete_fruit(self, fruit_id: int) -> None:
        for fruit in self.__fruits:
            if fruit.id == fruit_id:
                self.__fruits.remove(fruit)
                return

        raise HTTPException(
            status_code=404, detail=f"Fruit with id {fruit_id} not found"
        )
