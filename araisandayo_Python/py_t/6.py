print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x,y))

print(combs)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])

print([x for x in vec if x >= 0])

print([abs(x) for x in vec])

freshruit = ['  banana', '  loganberry ', 'passion fruit ']
print([weapon.strip() for weapon in freshruit])

print([(x, x**2) for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

print(list(zip(*matrix)))

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

t = 12345, 54321, 'hello!'
print(t[0])

print(t)

u = t, (1, 2, 3, 4, 5)
print(u)

v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = 8
singleton = 'hello',
print(len(singleton))
print(singleton)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)

print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)

print(a - b)

print(a | b)

print(a & b)

print(a ^ b)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))

print(sorted(tel.keys()))

print('guido' in tel)

print('jack' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print({x: x**2 for x in (2, 4, 6)})

print(dict(sape=4139, guido=4127, jack=4098))