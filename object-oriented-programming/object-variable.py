'''
This is an example for OBJECT VARIABLE 
'''

class varObject:

    def __init__(self, messagess):
        self.messagess=messagess


firstObject=varObject('Message from first created object')
print(firstObject.messagess)

secondObject=varObject('Message from second created object')
print(secondObject.messagess)
