class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))

for char in rev:
    print(char)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

print(sum(i*i for i in range(10)))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x, y in zip(xvec, yvec)))

from math import pi, sin
sine_table = {x:sin(x*pi/180) for x in range(0, 91)}

#unique_words = set(word for line in page for word in line.split())

#valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
