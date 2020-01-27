'''
a, b = 0, 1

while b < 10:
    print(b)
    a, b, = b, a+b

i = 256*256
print('THe value of i is', i)

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b


x = int(input("整数を入れてください:"))
if x < 0:
    x = 0
    print('負数をゼロとする')
elif x == 0:
    print('ゼロ')
elif x == 1:
    print('ひとつ')
else:
    print('もっと')
'''

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)

for i in range(5):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

while True:
    pass

class MyEmptyClass:
    pass

def initlog(*args):
    pass

