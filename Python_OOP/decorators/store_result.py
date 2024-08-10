class store_result:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open('result.txt', 'a+') as file:
            func_result = self.function
            file.write(f"Function {self.function.__name__} was called. Result {func_result}\n")

        return func_result