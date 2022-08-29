'''
this is program for "Return Variable Function" using the function.
'''

def return_variable_function(firstvar,secondvar):
    print(firstvar,'\t',secondvar)

    if firstvar>secondvar:
        return firstvar
    elif secondvar>firstvar:
        return secondvar
    else:
        return 'Both are equal'

print(return_variable_function(6,5))
