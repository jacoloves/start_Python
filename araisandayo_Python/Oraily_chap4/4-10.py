
def test(func):
    def new_function(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return new_function



@test
def add_int(a, b):
    print(a + b)

add_int(3, 5)