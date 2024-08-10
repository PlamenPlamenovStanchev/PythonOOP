class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "Value is not float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        int_value = 0
        for i in range(len(value)):
            if value[i] in roman_numerals:
                if i + 1 < len(value) and roman_numerals[value[i]] < roman_numerals[value[i + 1]]:
                    int_value -= roman_numerals[value[i]]
                else:
                    int_value += roman_numerals[value[i]]



    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "Wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "Wrong type"
