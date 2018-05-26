text="""おはよう
こんにちは
こんばんは"""

with open('hello.txt', 'w', encoding='cp932') as file:
	file.write(text)

with open('hello.txt', 'r', encoding='cp932') as file:
	src = file.read()
	print(src)