#リスト内包表記
#例1
'''
numbers = [1,5,6,11,9,5,7,3]
squares = [num**2 for num in numbers]
print(squares)
'''

#例2
'''
words = ['python','django','tkinter']
one_words = [char for word in words for char in word]
print(one_words)
'''

#例3
'''
odd_numbers = [x for x in range(1,11) if x % 2 == 1]
print(odd_numbers)
'''

#例3
'''
table = [[x *y for x in range(1, 10)] for y in range(1,10)]
print(table)
'''

#例4
'''
table = [[None for x in range(5)] for y in range(5)]
print(table)
'''

#例5
'''
dicts = {x:'デフォルト値' for x in range(10)}
print(dicts)
'''

#例6
'''
score = {'math':80, 'eng':20}
new_score = {value:key for key, value in score.items()}
print(new_score)
'''

#ジェネレーター内包表記
numbers = [1,5,6,11,3,5,7,3]
square_gen = (num**2 for num in numbers)
for num in square_gen:
	print(num)