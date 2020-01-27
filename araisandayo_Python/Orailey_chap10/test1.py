from datetime import date
now = date.today()
fout = open('today.txt', 'wt')
print(now, file=fout)
fout.close()
