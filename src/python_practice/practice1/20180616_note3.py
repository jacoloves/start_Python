month = 6

if month in {12, 1, 2}:
	season = '冬'
elif month in {3, 4, 5}:
	season = '春'
elif month in {6, 7, 8}:
	season = '夏'
elif month in {9, 10, 11}:
	season = '秋'
else:
	season = '不明'

msg = (str(month)) + '月の季節は、' + season + 'です。'
print(msg)
