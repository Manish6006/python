'''
While is called looping statement and while loop comes with additional else clause
'''
number = 23
running = True

try:
    while running:
        guess = int(input('Enter an integer : '))
        
        if guess == number:
            print('Congratulations, you guessed it.')
            # this causes the while loop to stop
            running = False
        elif guess < number:
            print('No, it is a little higher than that.')
        else:
            print('No, it is a little lower than that.')
    else:
        print('The while loop is over.')
except:
    print('Accept only Integer value')
finally:
    print('Done')