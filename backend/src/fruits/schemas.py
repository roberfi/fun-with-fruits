from typing import Annotated

from pydantic import BaseModel, BeforeValidator, Field

CapitalizedStr = Annotated[str, BeforeValidator(lambda raw: raw.capitalize())]

FRUIT_ID_DESCRIPTION = "The fruit's unique identifier"
FRUIT_NAME_DESCRIPTION = "The fruit's name"
FRUIT_COLOR_DESCRIPTION = "The fruit's color"


class Fruit(BaseModel):
    id: int = Field(description=FRUIT_ID_DESCRIPTION)
    name: CapitalizedStr = Field(description=FRUIT_NAME_DESCRIPTION)
    color: CapitalizedStr = Field(description=FRUIT_COLOR_DESCRIPTION)


class FruitCreate(BaseModel):
    name: CapitalizedStr = Field(description=FRUIT_NAME_DESCRIPTION)
    color: CapitalizedStr = Field(description=FRUIT_COLOR_DESCRIPTION)


class FruitUpdate(BaseModel):
    color: CapitalizedStr | None = Field(default=None, description=FRUIT_COLOR_DESCRIPTION)
