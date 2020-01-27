class Thing2():
    def __init__(self, name):
        self.name = name

letters = Thing2('abs')

print(letters.name)

class Thing3(Thing2):
    pass


letters = Thing3('xyz')
print(letters.name)