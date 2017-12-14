number = 23
running = True

while running:
    guess = int(input("Enter an Integer :"))
    if guess == number:
        print('Congratulations, you guessed it!')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
# 此处的else可以去掉
else:
    print('The while loop is over.')

print('Done')
