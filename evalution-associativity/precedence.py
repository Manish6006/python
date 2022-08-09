'''
This is an example for evaluate based on precedence order
'''
aInt=None
bInt=None
try:
    aInt=int(input('enter the first integer value\n'))
    bInt=int(input('enter the second integer value\n'))
    #without parentheses, If precedence order is same
    result= aInt + bInt - aInt
    print('the final value is ',result,'\n')

    #without parentheses, If precedence order is different
    result= aInt + bInt * aInt
    print('the final value is ',result,'\n')

    #with parentheses, If precedence order is same
    result= aInt + (bInt - aInt)
    print('the final value is ',result,'\n')

    #with parentheses, If precedence order is different
    result= (aInt + bInt) * aInt
    print('the final value is ',result,'\n')

except:
    print('Only Integer value is accepted')

finally:
    print('the program is end')


