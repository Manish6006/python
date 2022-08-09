'''
FOR loop to print the series of the number using range() function and else clause also work for the if statement
'''
firstValue=None
lastValue=None
try:
    firstValue=int(input('enter the starting value : '))
    lastValue=int(input('enter the last value : '))
    for i in range(firstValue,lastValue):
        print(i,end=' ')
    else:
        print('if statement is completed')
except:
    print('Integer value is only accepted')
finally:
    print('the exception block is done')