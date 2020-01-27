def get_odds(i=0, last=10):
    number = i
    while number < last:
        if number % 2 == 1:
            yield number
        number += 1

ranger = get_odds(range(10))

for x in ranger:
    print(x)