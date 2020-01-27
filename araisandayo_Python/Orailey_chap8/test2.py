writer = ''
fin = open('test1', 'rt')
writer = fin.read()
fin.close()

fout = open('test2', 'wt')
fout.write(writer)
fout.close()