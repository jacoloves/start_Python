while True:
	user_input = input()
	if user_input == 'exit':
		break
	elif user_input == 'skip':
		continue
	message = 'あなたの入力は{0}でした'.format(user_input)
	print(message)


names = ['田中太郎','佐藤次郎','鈴木三郎']
for name in names:
	if name.endswith('三郎'):
		print('いました')
		break
else:
	print('いませんでした')