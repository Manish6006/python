'''
This is an example to CREATE INHERITANCE CLASS
'''

from optparse import Values


class baseClass:
    def __init__(self, iterable):
        self.items_list=[]
        self.__update(iterable)
    
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    
    __update=update

class childClass(baseClass):
    def update(self, key, value):
        for item in zip(keys,values):
            self.items_list.append(item)

childObject=childClass()
childObject.update(5,6)
print(childObject.items_list)
        