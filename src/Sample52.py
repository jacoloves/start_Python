your_input = input('数字を入れて >')
try:
	number = int(your_input)
	print(10 / number)
except ValueError:
	print('文字が入力されました')
except ZeroDivisionError:
	print('0はだめです')
except:
	print('それ以外')