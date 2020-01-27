class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
c.radius
c.diameter

c.radius = 7
c.diameter = 20