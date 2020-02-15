import reprlib
print(reprlib.repr(set('supercalifragilosticexpialidocious')))

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
print(pprint.pprint(t, width=30))

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

import locale
#locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))

from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
print(t.safe_substitute(d))

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

#fmt = input('どのようにリネームしますか（%d- 日付 %n- 番号 %f- 形式）:')

# t = BatchRename(fmt)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=date, n=i, f=ext)
#     print('{0} --> {1}'.format(filename, newname))

import struct

# with open('myfile.zip', 'rb') as f:
#     data = f.read

# start = 0
# for i in range(3):
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(dilename, hex(crc32), comp_size, uncomp_size)

#     start += extra_size 

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished backeground zip of:', self.infile)

background = AsyncZip('dydata.txt', 'myarchive.zip')
background.start()
print('メインプログラムは表で動き続けています。')

background.join()
print('メインプログラムはバックグラウンド処理の終了まで待ってました。')