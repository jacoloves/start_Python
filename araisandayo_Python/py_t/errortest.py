class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# try:
# #     raise  KeyboardInterrupt
# # finally:
# #     print('Goodbye, world!')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("ゼロ除算！")
    else:
        print("答えは", result)
    finally:
        print("finally節実行中")

print(divide(2, 1))

print(divide(2, 0))

# print(divide("2", "1"))


