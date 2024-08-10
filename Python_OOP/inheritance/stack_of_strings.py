from typing import List


class Stack:
    def __init__(self)-> None:
        self.data: List[str] = []

    def push(self, element: str)-> str:
        self.data.append(element)

    def pop(self)-> str:
        return self.data.pop()

    def top(self)-> str:
        return self.data[-1]

    def is_empty(self)-> bool:
        return True if not self.data else False

    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"


