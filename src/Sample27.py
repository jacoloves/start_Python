def decorator(fuction):
	print('decorator')
	return fuction

@decorator # say_hello = decorator(say_hello)
def say_hello():
	print('hello')

say_hello()