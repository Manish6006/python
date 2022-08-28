'''
this is program for argument parameters using functions
'''
a=None
b=None
try:
    a=int(input('enter the value of a : '))
    b=int(input('enter the value of b : '))
    def function_with_parameters(a,b):
        if a>b:
            print('a value', a, 'is greater than b value', b,'\n') 
        elif b>a:
            print('b value', b, 'is greater than a value', a,'\n')
        elif a==b:
            print('both values are same\n')
        else:
            print('both values are not same\n')
    function_with_parameters(a,b)
except:
    print('something is wrong\n')
finally:
    print('The program is end\n')