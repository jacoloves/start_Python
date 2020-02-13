import os
print(os.getcwd())
#os.chdir('/server/accesslogs')
#print(os.system('mkdir today'))

import glob
print(glob.glob('*.py'))

import sys

print(sys.argv)

sys.stderr.write('Warning, log file not found starting a new one\n')

import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print('tea for too'.replace('too', 'two'))

import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as responce:
    for line in responce:
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:
            print(line)