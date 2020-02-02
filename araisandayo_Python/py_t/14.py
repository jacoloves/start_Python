import sys

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x=', x)
    print('y=', y)

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('ランタイムエラーを処理します；', err)

# raise NameError('HiThere')

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('例外が飛んでった！')
#     raise

