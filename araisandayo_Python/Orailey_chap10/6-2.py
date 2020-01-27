import os
os.symlink('oops.txt', 'jeepers.txt')
print(os.path.islink('jeepers.txt'))