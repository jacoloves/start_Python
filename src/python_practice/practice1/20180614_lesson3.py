'''
tp = (10, 'a', True)
tp[0]
tp[1]
tp[2]
'''

#(100, 'a') + (200, 'b')
#(100, 'a') * 3

'''
tp = (10, 'a')
tp += (20, 'b')
tp
tp *= 2
'''

#range(10)
#range(5, 11)
#range(10, 20, 2)

'''
rg = range(10, 20, 2)
rg[0]
rg[1]
rg[2]
'''

'''
list1 = [100, 200, 300]
tpl1 = (123, 'ok', True)
rng1 = range(10, 20)
result = list1 + list(tpl1) + list(rng1)
result
'''

'''
st = {'hi', 'hello', 'ok'}
st.add('welcome')
st.remove('ok')
st
'hello' in st
'''

'''
str1 = {10, 20, 30, 40, 50}
str2 = {0, 20, 40, 60, 80}
str1 & str2
str1 ^ str2
str1 - str2
'''

dc = {'a':100, 'b':200, 'c':300}
dc['d'] = 1000
dc['a'] = dc['b'] + dc['c']
dc