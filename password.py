n = 12

def func():

    global n

    print('Value of n is', n)

    n = 7

    print('Changed global n to', n)

func()

print('Value of n is now', n)