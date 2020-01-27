import os
#os.mkdir('poems')
#os.mkdir('poems/mcintyre')
#print(os.listdir('poems'))

fout = open('poems/mcintyre/the_good_man', 'wt')
print(fout.write('''Cheerful and happpy was his mood,
He to the poor was kind and good,
And he oftm times did find them food,
Aloso supplies of coal and wood,
He never spake a word was rude,
And cheer'd thoese did o'er sorrows brood,
He passes away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
'''))
fout.close()

print(os.listdir('poems/mcintyre'))