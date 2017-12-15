try:
    text = input('Enter something:')
except EOFError:
    print('\nWhy did you do an EOF on me?')
except KeyboardInterrupt:
    print('\nYou canceled the operation.')
else:
    print('\nYou entered {}'.format(text))
