poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

print(len(poem))

fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity2', 'wt')
print(poem, file=fout)
fout.close()

fout = open('relativity3', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity4', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close()