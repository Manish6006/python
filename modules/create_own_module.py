'''
This program is an example of CREATING OWN MODULE
'''

def outer_function(message):
    print('message from outer function is : ', message)

def inner_function(message):
    outer_function('this is the message from outer function as argument')
    print('message from inner function is : ', message)
inner_function('this is the message from outer function as argument')

__version__='0.1'
