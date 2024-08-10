class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, new_radius: float):
        self.radius = new_radius

    def get_area(self):
        return Circle.pi * self.radius ** 2
    #     return self.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * self.radius * Circle.pi
#       return 2 * self.radius * self.pi

