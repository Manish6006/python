'''
This program is an example of IMPORTING CREATED OWN MODULE
'''

import create_own_module

create_own_module.inner_function('this is calling from another program as part of module')

print('Version', create_own_module.__version__)
