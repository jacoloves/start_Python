text="""おはよう
こんにちは
こんばんは"""

file = open('hello.txt', 'w', encoding='utf-8')

file.write(text)

file.close()