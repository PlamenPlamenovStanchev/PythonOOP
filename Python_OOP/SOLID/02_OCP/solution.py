from abc import ABC,abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Turtle(Animal):
    def make_sound(self):
        return "Turtle sound"


class Pig(Animal):
    def make_sound(self):
        return "Oink Oink mother...."


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

