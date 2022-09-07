'''
This is an example for CREATING __INIT__ METHOD INSIDE THE CLASS
'''

from unicodedata import name


class init_test:
    def __init__(self,name):
        self.name=name
    
    def secondMethod(self):
        print('The name is :', self.name)
    

childObject=init_test('Snowdon')
childObject.secondMethod()
        