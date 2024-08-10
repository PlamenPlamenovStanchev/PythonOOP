from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        try:
            return reduce(lambda x, y: x / y, args)
        except ZeroDivisionError:
            return("Only God can divide by zero and Chick Norris of course!")

        
