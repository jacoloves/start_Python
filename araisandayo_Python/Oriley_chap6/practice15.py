class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill ans a', self.tail.length, 'tail')

tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()

from collections import namedtuple
Duck = namedtuple('Duck', 'bill trail')
duck = Duck('wide orange', 'long')
duck.bill
duck.trail

duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)
duck_dict['color'] = 'green'
print(duck_dict)