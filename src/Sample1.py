for i in range(1, 101):
	if i % 15 == 0:
		print('Fizz Buzz', end=' ')
	elif i % 5 == 0:
		print('Buzz', end=' ')
	elif i % 3 == 0:
		print('Fizz', end=' ')
	else:
		print(i, end=' ')

for i in range(1, 101):
	message = ''
	if i % 15 == 0:
		message = 'Fizz Buzz'
	elif i % 5 == 0:
		message = 'Buzz'
	elif i % 3 == 0:
		message = 'Fizz'
	else:
		message = i
	print(message, end=' ')


for i in range(1, 101):
	message = ''
	if i % 3 == 0:
		message += 'Fizz'

	if i % 5 == 0:
		message = 'Buzz'

	print(message or i, end=' ')

