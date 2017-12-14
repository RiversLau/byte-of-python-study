def func(a, b=5, c=10):
    print('a is', a, "and b is", b, "and c is", c)


func(10)
func(3, c=20)
func(20, b=10, c=10)
func(c=200, a=100)
