'''
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib(2000))

print(fib)
f = fib
print(f(100))
print(fib(0))

def fib2(n):
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
f100 = fib2(100)
print(f100)

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise  OSError('非協力的ユーザー')
        print(complaint)

ask_ok('Do you really want to quit!')
'''

'''
i = 5
def f(arg=i):
    print(arg)

i = 6
f()
'''

'''
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
'''

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("--Lovely plumage, the", type)
    print("--It's", state, "!")


def function(a):
    pass

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopleeper="Muchael Plain",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))