x = 50


def func(a):
    print('x is', a)
    a = 2
    print('Change local x to', a)


func(x)
print('x is still', x)
