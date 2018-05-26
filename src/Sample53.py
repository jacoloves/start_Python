your_input = input("10 / nの、nにあたる数を好きに入れてください >")
if not your_input.isnumeric():
	print('文字が入力されました')
elif your_input == '0':
	print('0で割ったらいけません')
else:
	number = int(your_input)
	print(10 /number)
