import logging
logging.debug('Debbug information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occured')
logging.critical('Critical error -- shutting down')

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
print(gc.collect())
#print(d['primary'])

from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
print([heappop(data) for i in range(3)])

from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))

print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10) == 1.0)

getcontext().prec = 36
print(Decimal(1)/Decimal(7))