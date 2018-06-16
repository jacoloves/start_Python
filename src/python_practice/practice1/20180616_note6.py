'''
num = 12345
n = 2
res = []
while n <= num // 2:
	if num % n == 0:
		res += [n]
	n += 1
print(str(num) + 'の約数')
print(res)
'''

'''
print('start.')
num = 0
while num == 0:
	num = 0
print('end.')
'''

'''
num = 10203
n = num // 2
print('計算開始......')
while num % n != 0:
	n -= 1
else:
	print('※解けました。')
msg = str(num) + 'の最大約数:' + str(n)
print(msg)
'''

num = 9876
n = num // 2
print('計算開始.......')
while True:
	if num % n ==0:
		break
	n -= 1
msg = str(num) + 'の最大約数:' + str(n)
print(msg)
