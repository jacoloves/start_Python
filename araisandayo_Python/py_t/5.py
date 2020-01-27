def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

print(f(0))

print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

print(pairs)

def my_function():
    '''
    テストですと！
    わははは！
    :return:
    '''
    pass

print(my_function.__doc__)

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotaions:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)

a.append(333)
print(a)

print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)

print(a.pop())

print(a)


stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

print(stack.pop())

print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)