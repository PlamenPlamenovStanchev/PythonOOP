from typing import List, Type

from project.animals.animal import Mammal
from project.food import Food, Meat, Vegetable, Fruit


class Mouse(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Vegetable, Fruit]

    @property
    def weight_increment(self) -> float:
        return 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Cat(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Vegetable]

    @property
    def weight_increment(self) -> float:
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Dog(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Tiger(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"

