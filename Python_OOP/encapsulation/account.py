class Account:
    def __init__(self, id: int, balance: int, pin: int) -> None:
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> str:
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin: str, new_pin: str) ->str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"

