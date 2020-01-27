import string
import re
printables = string.printable
print(len(printables))
print(printables[0:50])
print(printables[50:])
print(re.findall('\d', printables))
print(re.findall('\w', printables))
print(re.findall('\s', printables))

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall('\w', x))