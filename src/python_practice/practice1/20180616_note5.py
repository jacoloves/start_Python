'''
data = {'国語':98, '数学':82, '理科':67, '社会':59, '英語':65}
total = 0
for k in data:
	print(k + ':' + str(data[k]))
	total += data[k]
ave = total // len(data)
msg = '合計：' + str(total) + ' 平均：' + str(ave)
print(msg)
'''

'''
data = {'国語':98, '数学':82, '理科':67, '社会':59, '英語':65}
total = 0
for k in data:
	print(k + ':' + str(data[k]))
	total += data[k]
else:
	print('======データは以上です======')
ave = total // len(data)
msg = '合計：' + str(total) + ' 平均：' + str(ave)
print(msg)
'''

'''
data = {'国語':98, '数学':82, '理科':67, '社会':59, '英語':65}
total = 0
for k in data:
	if k in {'国語', '数学', '英語'}:
		print(k + ':' + str(data[k]))
	else:
		continue
	total += data[k]
else:
	print('======データは以上です======')
ave = total // len(data)
msg = '合計:' + str(total) + ' 平均:' + str(ave)
print(msg)
'''