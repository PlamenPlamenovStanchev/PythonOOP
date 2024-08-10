from typing import List, Union

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum(w.salary for w in self.workers)
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_money_for_care = sum(a.money_for_care for a in self.animals)
        if self.__budget < total_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        # pass
        # lions = []
        # tigers = []
        # cheetahs = []
        # for animal in self.animals:
        #     if animal.__class__.__name__ == "Lion":
        #         lions.append(repr(animal))
        #     if animal.__class__.__name__ == "Tiger":
        #         tigers.append(repr(animal))
        #     if animal.__class__.__name__ == "Cheetah":
        #         cheetahs.append(repr(animal))
        #
        #     result = [f'You have {len(self.animals)} animals', f'----- {len(lions)} Lions:']
        #     result.extend(lions)
        #     result.append(f'----- {len(tigers)} Tigers:')
        #     result.extend(tigers)
        #     result.append(f'----- {len(cheetahs)} Cheetahs:')
        #     result.extend(cheetahs)
        #     return '\n'.join(result)
        return self.__print_status(self, self.animals, 'Lion', 'Tiger', 'Cheetah')

    def workers_status(self) -> str:
        # keepers = []
        # caretakers = []
        # vets = []
        # for worker in self.workers:
        #     if worker.__class__.__name__ == "Keeper":
        #         keepers.append(repr(worker))
        #     if worker.__class__.__name__ == "Caretaker":
        #         caretakers.append(repr(worker))
        #     if worker.__class__.__name__ == "Vet":
        #         vets.append(repr(worker))
        #
        #     result = [f'You have {len(self.animals)} animals', f'----- {len(keepers)} Keepers:']
        #     result.extend(keepers)
        #     result.append(f'----- {len(caretakers)} Caretakers:')
        #     result.extend(caretakers)
        #     result.append(f'----- {len(vets)} Vets:')
        #     result.extend(vets)
        #     return '\n'.join(result)
        #
        return self.__print_status(self, self.workers, 'Keeper', 'Caretaker', 'Vet')
    #
    @staticmethod
    def __print_status(self, category: List[Union[Animal, Worker]], *args) -> str:
        elements = {arg: [] for arg in args}
        for el in category:
            elements[el.__class__.__name__].append(repr(el))

        result = [f'You have {len(category)} {str(category[0].__class__.__bases__[0].__name__).lower()}s']
        for key in args:
            value = elements[key]
            result.append(f'----- {len(value)} {key}s:')
            result.extend(value)

        return '\n'.join(result)



