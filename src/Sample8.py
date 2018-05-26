text='追記'

file = open('hello.txt', 'x', encoding='utf-8')

file.write(text)

file.close()