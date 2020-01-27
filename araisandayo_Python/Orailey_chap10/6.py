import os
os.link('oops.txt', 'yikes.txt')
print(os.path.isfile('yikes.txt'))

