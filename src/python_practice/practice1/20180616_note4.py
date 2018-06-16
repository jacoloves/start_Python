'''
for word in ('Python', 'パイソン'):
	print(word)
'''

'''
for word in ('Python', 'パイソン', 'ぱいそん'):
	print('繰り返し')
'''

'''
data = [98, 76, 59, 86, 71, 64, 53, 99, 48]

total = 0
for n in data:
	total += n
ave = total // len(data)

msg = '合計：' + str(total) + '平均：' + str(ave)
print(msg)
'''

'''
num = 10

for i in range(num):
	print(i)
'''

'''
for i in range(1, 10):
	print(i)
print('--------------区切り線---------------')
for i in range(1, 10, 3):
	print(i)
'''

num = 1234
total = 0
for n in range(num+1):
	total += n

msg = str(num) + "までの合計：" + str(total)
print(msg)
