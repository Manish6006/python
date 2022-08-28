'''
this is program for create local variable and use inside the function using functions
'''

variable=None

try:
    variable=float(input('enter the value of variable : '))

    def function_with_variable(variable):
        print('global variable value is : ', variable,'\n')
        variable=None
        try:
            variable=float(input('enter the value of variable : '))
            print('local variable value is :', variable,'\n')
        except:
            print('something is missing\n')
    function_with_variable(variable)
except:
    print('something is missing out of functions\n')
finally:
    print('program is end\n')
