class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current_index = len(iterable)
        self.end_index = 0

    def __iter__(self):
        return self
        # return reversed(self.iterable)

    def __next__(self):
        self.current_index -= 1
        if self.current_index >= self.end_index:
            return self.iterable[self.current_index]
        raise StopIteration