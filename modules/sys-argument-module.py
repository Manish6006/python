'''
This program is an example of sys argument module 
'''
import sys


print('The command line arguments are: ')

for value in sys.argv:
    print(value)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
