# conditional using functions

first_var=input('\n enter the first name \n')
second_var=input('\n enter the last name \n')

def name_addition(first_var,second_var):
    if first_var=='xyz' and second_var=='abcd':
        return (first_var + second_var)
    elif second_var=='xyz' and first_var=='abcd':
        return (first_var + second_var)
    else:
        return 'no matching name found'
print('\n result = ',name_addition(first_var,second_var),'\n')
