class MyClass:
    i = 12345
    def f(self):
        return 'hello world'
    def __init__(self):
        self.data = []


class Complex:
    def __init__(self, replpart, imagpart):
        self.r = replpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)