def print_max(x, y):
    '''Prints the maximum of two numbers.

    the two value must be integers.'''
    # 如果可能，将其转换为整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(2, 6)
print(print_max.__doc__)
