#"123" + 45
#"123" + str(45)
#int("123") + 45
#0.1 + 0.1 + 0.1
#a = 1
#a = a + 10
#print(a)
#a = 1
#a += 10
#print(a)
#print(True and False)
#print(True or False)
#print(not True)
#1
#'1'
#str(1)
#[1,2,3]
#if True:
#	print('python')
#for i in [0,1]:
#	print(i)
#0b1010 << 1 #2 0
#0b1010 << 2 # 40
#0b1010 >> 1 # 5
#0b1010 >> 2 # 2

'''
#list2-1
name = "Taro"
age = "35 years old"
msg = "Hello! I'm " + name + ", " + age + "."
print(msg)
'''

'''
#list2-2
name = 'Taro'
age = '35 years old'
msg = "Hello! I'm " + name + ", " \
      + age + '.'
print(msg)
'''

'''
#list2-3
name = 'Taro' #名前
age = '35 years old' #年齢
# 名前と文字列を組み合わせて表示する
msg = "Hello! I'm " + name + ", " + age + "."
print(msg)
'''

'''
#list2-4
name = 'Taro'
age = '35 years old'
msg = f"HellO! I'm {name}, {age}."
print(msg)
'''

'''
price = 12300
f'{price}円の税込価格は、{price * 1.08}円です。'
'''

'''
#list2-5
# 金額を変数に代入する
price = 123400
# 税率を変数に代入する
TAX = 1.08
'''
金額に税率をかけた結果を計算できる。
これで消費税込み価格が計算できる
'''
print(price * TAX)
'''
