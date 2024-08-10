from project.computer_types.computer import Computer


class Laptop(Computer):

    @property
    def available_processors(self):
        return {
            "AMD Ryzen 95950X": 900,
            "Intel - Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    @property
    def max_ram(self) -> int:
        return 64

    def __str__(self):
        return "laptop"

