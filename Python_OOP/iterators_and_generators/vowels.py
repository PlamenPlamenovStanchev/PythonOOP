class vowels:
    def __init__(self, string)-> None:
        self.string = string
        self.all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.vowels_from_string = [el for el in self.string if el.lower() in self.all_vowels]
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index < len(self.vowels_from_string):
            return self.vowels_from_string[self.current_index]
        raise StopIteration