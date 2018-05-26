try:
	file = open('hello.txt','x',encoding='utf-8')
except FileExistsError:
	print('ファイルが概に存在しています')
else:
	file.write('hello')
finally:
	file.close()