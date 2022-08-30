'''
This program is an example of FROM IMPORTING CREATED OWN MODULE
'''
from create_own_module import inner_function,__version__

inner_function('this is calling FROM module')
print(__version__)