'''
this is program for define x with global keyword using the function.
'''
'''
this is program for create local x and use inside the function using functions
'''
x = 50


def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)