# 4-1
guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else :
    print("just right")

# 4-2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("fount it!")
    elif start > guess_me:
        print("oops")
        break
    start += 1

# 4-3

