class Dog:

    tricks = []
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fibo')
e = Dog('Buddy')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

d.add_trick('ころがる')
e.add_trick('死んだふり')
print(d.tricks)
print(e.tricks)
