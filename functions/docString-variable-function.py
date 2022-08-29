'''
this is program for "DocString Variable Function" using the function.
'''
def docstring_variable_function(firstvar,secondvar):
    

    '''prints the maximum of two numbers, the two values must be integers'''

    print(firstvar,'\t',secondvar)

    if firstvar>secondvar:
        print('firstvar is max ', firstvar,'\n')
    elif secondvar>firstvar:
        print('secondvar is max ', secondvar,'\n')
    else:
        print('both are same')

docstring_variable_function(6,3)
print(docstring_variable_function.__doc__)