class Smartphone:
    def __init__(self, memory: float) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) ->None:
        # self.is_on = not self.is_on
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, app: str, app_memory: float)-> str:
        if self.memory >= app_memory and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        elif self.memory >= app_memory and  not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

